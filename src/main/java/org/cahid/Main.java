package org.cahid;

import org.cahid.moves.MoveFactory;
import org.optaplanner.core.api.solver.Solver;
import org.optaplanner.core.api.solver.SolverFactory;
import org.optaplanner.core.config.heuristic.selector.move.factory.MoveListFactoryConfig;
import org.optaplanner.core.config.localsearch.LocalSearchPhaseConfig;
import org.optaplanner.core.config.localsearch.decider.acceptor.LocalSearchAcceptorConfig;
import org.optaplanner.core.config.localsearch.decider.forager.FinalistPodiumType;
import org.optaplanner.core.config.localsearch.decider.forager.LocalSearchForagerConfig;
import org.optaplanner.core.config.score.director.ScoreDirectorFactoryConfig;
import org.optaplanner.core.config.solver.SolverConfig;
import org.optaplanner.core.config.solver.termination.TerminationCompositionStyle;
import org.optaplanner.core.config.solver.termination.TerminationConfig;
import org.optaplanner.core.impl.heuristic.selector.move.factory.MoveListFactory;

import java.io.IOException;
import java.util.List;

public class Main {
    public static final String RES = "src/main/resources/";



    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
//        Network speedup = new Network(RES + "test/sparse16.txt");
//        SolverFactory.createFromXmlResource("planning_config.xml").buildSolver().solve(speedup);

        if (args.length != 1) {
            System.out.println("Usage: java -jar <executable> <filename>");
            return;
        }
        String filename = args[0];

        long startTime = System.nanoTime();
        Network network = new Network(filename);

        MoveListFactoryConfig mlf = new MoveListFactoryConfig();
        mlf.setMoveListFactoryClass(MoveFactory.class);

        SolverFactory<Network> solverFactory = SolverFactory.create(new SolverConfig()
                .withSolutionClass(Network.class)
                .withEntityClasses(Path.class)
                .withScoreDirectorFactory(new ScoreDirectorFactoryConfig()
                        .withIncrementalScoreCalculatorClass(IncrementalCalculator.class))
                .withTerminationConfig(new TerminationConfig()
                        .withTerminationCompositionStyle(TerminationCompositionStyle.OR)
                        .withSecondsSpentLimit(60L)
                        .withTerminationClass(BestSolutionFound.class))
                .withPhases(new LocalSearchPhaseConfig()
                        .withMoveSelectorConfig(mlf)
                        .withAcceptorConfig(new LocalSearchAcceptorConfig()
                                .withEntityTabuSize(7))
                        .withForagerConfig(new LocalSearchForagerConfig()
                                .withAcceptedCountLimit(1000)
                                .withFinalistPodiumType(FinalistPodiumType.STRATEGIC_OSCILLATION))));

        Solver<Network> solver = solverFactory.buildSolver();

        Network solution = solver.solve(network);

        long endTime = System.nanoTime();

        System.out.println(solution.getScore());
        System.out.println("Execution time: " + (endTime - startTime) / 1000000000.0);

        // measure time
//        for (int i = 0; i <= 26; i++) {
//            System.out.println("Test " + i);
//            long startTime = System.nanoTime();
//            Network network = new Network(RES + "test/dense" + i + ".txt");
//
//            SolverFactory<Network> solverFactory = SolverFactory.createFromXmlResource("planning_config.xml");
//            Solver<Network> solver = solverFactory.buildSolver();
//
//            Network solution = solver.solve(network);
//
//            long endTime = System.nanoTime();
//
//            System.out.println(solution.getScore());
//            System.out.println("Execution time: " + (endTime - startTime) / 1000000000.0);
//            sb.append("Test " + i + "\n");
//            sb.append("Execution time: " + (endTime - startTime) / 1000000000.0 + "\n");
//            sb.append("Score: " + solution.getScore() + "\n");
//
//        }

//        System.out.println("--------------------------------");
//        System.out.println(sb);

    }
}