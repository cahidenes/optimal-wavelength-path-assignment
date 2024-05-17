package org.cahid.moves;

import org.cahid.Network;
import org.cahid.Path;
import org.optaplanner.core.api.score.director.ScoreDirector;
import org.optaplanner.core.impl.heuristic.move.AbstractMove;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class ExtendPathMove extends AbstractMove<Network> {
    Path path;
    int neighbor;
    public ExtendPathMove(Path path, int neighbor) {
        this.path = path;
        this.neighbor = neighbor;
    }

    @Override
    protected AbstractMove<Network> createUndoMove(ScoreDirector<Network> scoreDirector) {
        return new RemovePathMove(path, 1);
    }

    @Override
    protected void doMoveOnGenuineVariables(ScoreDirector<Network> scoreDirector) {
        scoreDirector.beforeVariableChanged(path, "path");

        path.getPath().add(neighbor);
        scoreDirector.afterVariableChanged(path, "path");
        scoreDirector.triggerVariableListeners();
    }

    @Override
    public boolean isMoveDoable(ScoreDirector<Network> scoreDirector) {
        return true;
    }

    @Override
    public String getSimpleMoveTypeDescription() {
        return "Extend path " + path.getId() + " to " + neighbor;
    }

    @Override
    public String toString() {
        return "extend " + path.getId() + " " + neighbor;
    }

    @Override
    public Collection<?> getPlanningValues() {
        return Collections.singletonList(path);
    }

    @Override
    public Collection<?> getPlanningEntities() {
        return Collections.singletonList(path);
    }
}
