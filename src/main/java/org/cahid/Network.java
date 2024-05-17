package org.cahid;

import org.optaplanner.core.api.domain.solution.PlanningEntityCollectionProperty;
import org.optaplanner.core.api.domain.solution.PlanningScore;
import org.optaplanner.core.api.domain.solution.PlanningSolution;
import org.optaplanner.core.api.domain.solution.ProblemFactCollectionProperty;
import org.optaplanner.core.api.domain.valuerange.ValueRangeProvider;
import org.optaplanner.core.api.score.buildin.hardmediumsoft.HardMediumSoftScore;
import org.optaplanner.core.api.score.buildin.hardsoft.HardSoftScore;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

@PlanningSolution
public class Network {

    private ArrayList<ArrayList<Integer>> topology = new ArrayList<>();
    private int[][] distances;
    private int availableWavelengths;

    @ValueRangeProvider(id="wavelengthRange")
    private ArrayList<Integer> wavelengthRange = new ArrayList<>();
    @ValueRangeProvider(id="nodeRange")
    private ArrayList<Integer> nodeRange = new ArrayList<>();

    @PlanningEntityCollectionProperty
    private ArrayList<Path> paths = new ArrayList<>();

    @PlanningScore
    private HardMediumSoftScore score;


    public Network(){}

    public Network(String filename) throws FileNotFoundException {
        Scanner input = new Scanner(new File(filename));
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            topology.add(new ArrayList<>());
        }

        int m = input.nextInt();
        for (int i = 0; i < m; i++) {
            int u = input.nextInt();
            int v = input.nextInt();
            topology.get(u).add(v);
            topology.get(v).add(u);
        }

        int l = input.nextInt();
        for (int i = 0; i < l; i++) {
            int s = input.nextInt();
            int d = input.nextInt();
            paths.add(new Path(i, s, d));
        }

        availableWavelengths = input.nextInt();
        input.close();

        distances = new int[n][n];

        // run dijkstra for each node
        for (int i = 0; i < n; i++) {
            int[] distance = dijkstra(i);
            System.arraycopy(distance, 0, distances[i], 0, n);
        }

        for (int i = 0; i < availableWavelengths; i++) {
            wavelengthRange.add(i);
        }

        for (int i = 0; i < n; i++) {
            nodeRange.add(i);
        }

        System.out.println("Number of paths: " + paths.size());

//        // Full constructor
        for (Path path: paths) {
            int cur = path.getSource();
            while (cur != path.getDestination()) {
                int min = Integer.MAX_VALUE;
                int next = -1;
                for (int neighbor: topology.get(cur)) {
                    if (path.getPath().contains(neighbor)) continue;
                    if (distances[neighbor][path.getDestination()] < min) {
                        min = distances[neighbor][path.getDestination()];
                        next = neighbor;
                    }
                }
                if (next == -1) break;
                path.getPath().add(next);
                cur = next;
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Path path: paths) {
                sb.append(path.getSource()).append(" -> ").append(path.getDestination()).append(": (");
                for (int node: path.getPath()) sb.append(node).append(" - ");
                sb.append("), wl = ").append(path.getWavelength());
                if (!path.isDone()) sb.append(" [NOT DONE] ");
                sb.append('\n');
        }
        return sb.toString();
    }

    private int[] dijkstra(int i) {
        int n = topology.size();
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[i] = 0;
        boolean[] visited = new boolean[n];
        for (int j = 0; j < n; j++) {
            int min = Integer.MAX_VALUE;
            int minIndex = -1;
            for (int k = 0; k < n; k++) {
                if (!visited[k] && distance[k] < min) {
                    min = distance[k];
                    minIndex = k;
                }
            }
            visited[minIndex] = true;
            for (int k = 0; k < topology.get(minIndex).size(); k++) {
                int v = topology.get(minIndex).get(k);
                if (!visited[v] && distance[minIndex] + 1 < distance[v]) {
                    distance[v] = distance[minIndex] + 1;
                }
            }
        }
        return distance;
    }


    // Getter and Setters
    public ArrayList<ArrayList<Integer>> getTopology() {
        return topology;
    }

    public void setTopology(ArrayList<ArrayList<Integer>> topology) {
        this.topology = topology;
    }

    public int[][] getDistances() {
        return distances;
    }

    public void setDistances(int[][] distances) {
        this.distances = distances;
    }

    public int getAvailableWavelengths() {
        return availableWavelengths;
    }

    public void setAvailableWavelengths(int availableWavelengths) {
        this.availableWavelengths = availableWavelengths;
    }

    public ArrayList<Path> getPaths() {
        return paths;
    }

    public void setPaths(ArrayList<Path> paths) {
        this.paths = paths;
    }

    public HardMediumSoftScore getScore() {
        return score;
    }

    public void setScore(HardMediumSoftScore score) {
        this.score = score;
    }

}
