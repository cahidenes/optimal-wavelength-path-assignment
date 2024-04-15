package org.cahid;

import org.optaplanner.core.api.score.buildin.hardmediumsoft.HardMediumSoftScore;
import org.optaplanner.core.impl.phase.scope.AbstractPhaseScope;
import org.optaplanner.core.impl.phase.scope.AbstractStepScope;
import org.optaplanner.core.impl.solver.scope.SolverScope;
import org.optaplanner.core.impl.solver.termination.Termination;
import org.optaplanner.core.impl.solver.thread.ChildThreadType;

public class BestSolutionFound implements Termination<Network> {
    @Override
    public boolean isSolverTerminated(SolverScope<Network> solverScope) {
        HardMediumSoftScore score = (HardMediumSoftScore) solverScope.getBestScore();
        return score.getSoftScore() == 0 && score.getHardScore() == 0;
    }

    @Override
    public boolean isPhaseTerminated(AbstractPhaseScope<Network> abstractPhaseScope) {
        return false;
    }

    @Override
    public double calculateSolverTimeGradient(SolverScope<Network> solverScope) {
        return 0;
    }

    @Override
    public double calculatePhaseTimeGradient(AbstractPhaseScope<Network> abstractPhaseScope) {
        return 0;
    }

    @Override
    public Termination<Network> createChildThreadTermination(SolverScope<Network> solverScope, ChildThreadType childThreadType) {
        return null;
    }

    @Override
    public void phaseStarted(AbstractPhaseScope<Network> abstractPhaseScope) {

    }

    @Override
    public void stepStarted(AbstractStepScope<Network> abstractStepScope) {

    }

    @Override
    public void stepEnded(AbstractStepScope<Network> abstractStepScope) {

    }

    @Override
    public void phaseEnded(AbstractPhaseScope<Network> abstractPhaseScope) {

    }

    @Override
    public void solvingStarted(SolverScope<Network> solverScope) {

    }

    @Override
    public void solvingEnded(SolverScope<Network> solverScope) {

    }
}
