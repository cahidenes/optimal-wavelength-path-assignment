package org.cahid;

import org.optaplanner.core.api.score.buildin.hardmediumsoft.HardMediumSoftScore;
import org.optaplanner.core.api.score.calculator.IncrementalScoreCalculator;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class IncrementalCalculator implements IncrementalScoreCalculator<Network, HardMediumSoftScore> {
    HashMap<String, Integer> occupancy = new HashMap<>();
    int hard = 0, medium = 0, soft = 0;
    int lastSize = 0;
    int lastwl = -1;
    ArrayList<Integer> lastPath = new ArrayList<>();
    int[][] dist;
    @Override
    public void resetWorkingSolution(Network network) {
        hard = 0;
        medium = 0;
        soft = 0;
        occupancy = new HashMap<>();
        dist = network.getDistances();
        for (Path path : network.getPaths()) {
            if (path.isDone()) medium++;
            else {
                soft -= network.getDistances()[path.getPath().get(path.getPath().size() - 1)][path.getDestination()];
            }
            for (int i = 0; i < path.getPath().size() - 1; i++) {
                int src = path.getPath().get(i);
                int dst = path.getPath().get(i + 1);
                String edge = getEdge(src, dst, path.getWavelength());
                if (occupancy.containsKey(edge)) {
                    hard--;
                    occupancy.put(edge, occupancy.get(edge) + 1);
                } else {
                    occupancy.put(edge, 1);
                }
            }
        }
    }

    private String getEdge(int src, int dst, int wl) {
        if (src > dst) {
            int tmp = src;
            src = dst;
            dst = tmp;
        }
        return src + " " + dst + " " + wl;
    }

    @Override
    public void beforeEntityAdded(Object o) {
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    public void afterEntityAdded(Object o) {
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    public void beforeVariableChanged(Object o, String s) {
        Path path = (Path) o;

        // hard
        lastSize = path.getPath().size();
        lastwl = path.getWavelength();
        lastPath = new ArrayList<>(path.getPath());

//        for (int i = 0; i < path.getPath().size() - 1; i++) {
//            int src = path.getPath().get(i);
//            int dst = path.getPath().get(i + 1);
//            String edge = getEdge(src, dst, path.getWavelength());
//            if (occupancy.get(edge) > 1) {
//                hard++;
//            }
//            occupancy.put(edge, occupancy.get(edge) - 1);
//        }

        // medium
        if (path.getPath().get(path.getPath().size()-1) == path.getDestination()) {
            medium -= 1;
        }

        // soft
        soft += dist[path.getPath().get(path.getPath().size()-1)][path.getDestination()];
    }

    @Override
    public void afterVariableChanged(Object o, String s) {
        Path path = (Path) o;

        // hard
//        for (int i = 0; i < path.getPath().size() - 1; i++) {
//            int src = path.getPath().get(i);
//            int dst = path.getPath().get(i + 1);
//            String edge = getEdge(src, dst, path.getWavelength());
//            if (!occupancy.containsKey(edge)) occupancy.put(edge, 0);
//            occupancy.put(edge, occupancy.get(edge) + 1);
//            if (occupancy.get(edge) > 1) {
//                hard--;
//            }
//        }
        int cursize = path.getPath().size();
        if (cursize > lastSize) {
            // extended
            for (int i = lastSize-1; i < cursize-1; i++) {
                int src = path.getPath().get(i);
                int dst = path.getPath().get(i + 1);
                String edge = getEdge(src, dst, path.getWavelength());
                if (!occupancy.containsKey(edge)) occupancy.put(edge, 0);
                occupancy.put(edge, occupancy.get(edge) + 1);
                if (occupancy.get(edge) > 1) {
                    hard--;
                }
            }
        } else if (cursize < lastSize) {
            // removed
            for (int i = cursize-1; i < lastSize-1; i++) {
                int src = lastPath.get(i);
                int dst = lastPath.get(i + 1);
                String edge = getEdge(src, dst, lastwl);
                if (occupancy.get(edge) > 1) {
                    hard++;
                }
                occupancy.put(edge, occupancy.get(edge) - 1);
            }
        } else {
            // wavelength
            for (int i = 0; i < cursize-1; i++) {
                // add new wl
                int src = path.getPath().get(i);
                int dst = path.getPath().get(i + 1);
                String edge = getEdge(src, dst, path.getWavelength());
                if (!occupancy.containsKey(edge)) occupancy.put(edge, 0);
                occupancy.put(edge, occupancy.get(edge) + 1);
                if (occupancy.get(edge) > 1) {
                    hard--;
                }

                // remove old wl
                edge = getEdge(src, dst, lastwl);
                if (occupancy.get(edge) > 1) {
                    hard++;
                }
                occupancy.put(edge, occupancy.get(edge) - 1);
            }
        }

        // medium
        if (path.getPath().get(cursize-1) == path.getDestination()) {
            medium += 1;
        }

        // soft
        soft -= dist[path.getPath().get(cursize-1)][path.getDestination()];
    }

    @Override
    public void beforeEntityRemoved(Object o) {
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    public void afterEntityRemoved(Object o) {
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    public HardMediumSoftScore calculateScore() {
        return HardMediumSoftScore.of(hard, medium, soft);
    }
}
