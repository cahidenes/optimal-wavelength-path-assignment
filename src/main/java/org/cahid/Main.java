package org.cahid;

import org.optaplanner.core.api.solver.Solver;
import org.optaplanner.core.api.solver.SolverFactory;

import java.io.IOException;

public class Main {
    public static final String RES = "src/main/resources/";
    public static void main(String[] args) throws IOException {
        Network network = new Network(RES + "examples/dense1.txt");

        SolverFactory<Network> solverFactory = SolverFactory.createFromXmlResource("planning_config.xml");
        Solver<Network> solver = solverFactory.buildSolver();

        Network solution = solver.solve(network);

        System.out.println(solution.getScore());

    }
}