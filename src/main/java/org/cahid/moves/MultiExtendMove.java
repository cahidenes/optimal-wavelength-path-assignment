package org.cahid.moves;

import org.cahid.Network;
import org.cahid.Path;
import org.optaplanner.core.api.score.director.ScoreDirector;
import org.optaplanner.core.impl.heuristic.move.AbstractMove;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class MultiExtendMove extends AbstractMove<Network> {
    ArrayList<Integer> append;
    Path path;

    public MultiExtendMove(Path path, ArrayList<Integer> append) {
        this.path = path;
        this.append = append;
    }

    @Override
    protected AbstractMove<Network> createUndoMove(ScoreDirector<Network> scoreDirector) {
        return new RemovePathMove(path, append.size());
    }

    @Override
    protected void doMoveOnGenuineVariables(ScoreDirector<Network> scoreDirector) {
        scoreDirector.beforeVariableChanged(path, "path");
        for (int node: append) path.getPath().add(node);
        scoreDirector.afterVariableChanged(path, "path");
        scoreDirector.triggerVariableListeners();
    }

    @Override
    public boolean isMoveDoable(ScoreDirector<Network> scoreDirector) {
        return true;
    }

    @Override
    public String getSimpleMoveTypeDescription() {
        return "MultiExtendMove";
    }

    @Override
    public Collection<?> getPlanningEntities() {
        return Collections.singleton(path);
    }

    @Override
    public Collection<?> getPlanningValues() {
        return Collections.singleton(path);
    }
}
