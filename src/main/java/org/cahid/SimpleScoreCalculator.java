package org.cahid;

import org.optaplanner.core.api.score.buildin.hardmediumsoft.HardMediumSoftScore;
import org.optaplanner.core.api.score.calculator.EasyScoreCalculator;

import java.util.HashSet;

public class SimpleScoreCalculator implements EasyScoreCalculator<Network, HardMediumSoftScore> {
    @Override
    public HardMediumSoftScore calculateScore(Network network) {
        HashSet<String> set = new HashSet<>();
        int hard = 0, medium = 0, soft = 0;
        for (Path path : network.getPaths()) {
            if (path.isDone()) medium++;
            else {
                soft -= network.getDistances()[path.getPath().get(path.getPath().size() - 1)][path.getDestination()];
            }
            for (int i = 0; i < path.getPath().size() - 1; i++) {
                int src = path.getPath().get(i);
                int dst = path.getPath().get(i + 1);
                String edge = getEdge(src, dst, path.getWavelength());
                if (set.contains(edge)) {
                    hard--;
                } else {
                    set.add(edge);
                }
            }
        }
        return HardMediumSoftScore.of(hard, medium, soft);
    }

    private String getEdge(int src, int dst, int wl) {
        if (src > dst) {
            int tmp = src;
            src = dst;
            dst = tmp;
        }
        return src + " " + dst + " " + wl;
    }
}
