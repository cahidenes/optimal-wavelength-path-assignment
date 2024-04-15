package org.cahid.moves;

import org.cahid.Network;
import org.cahid.Path;
import org.optaplanner.core.api.score.director.ScoreDirector;
import org.optaplanner.core.impl.heuristic.move.AbstractMove;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class RemovePathMove extends AbstractMove<Network> {
    Path path;
    int removeCount;
    ArrayList<Integer> removedNodes;
    public RemovePathMove(Path path, int removeCount) {
        this.path = path;
        this.removeCount = removeCount;
        removedNodes = new ArrayList<>();
        for (int i = 0; i < removeCount; i++) {
            removedNodes.add(path.getPath().get(path.getPath().size()-1-i));
        }
    }

    @Override
    protected AbstractMove<Network> createUndoMove(ScoreDirector<Network> scoreDirector) {
        return new MultiExtendMove(path, removedNodes);
    }

    @Override
    protected void doMoveOnGenuineVariables(ScoreDirector<Network> scoreDirector) {
        scoreDirector.beforeVariableChanged(path, "path");
        for (int i = 0; i < removeCount; i++) {
            path.getPath().remove(path.getPath().size() - 1);
        }
        scoreDirector.afterVariableChanged(path, "path");
        scoreDirector.triggerVariableListeners();
    }

    @Override
    public boolean isMoveDoable(ScoreDirector<Network> scoreDirector) {
        return true;
    }

    @Override
    public String getSimpleMoveTypeDescription() {
        return "Remove " + removeCount + " from path " + path.getId();
    }

    @Override
    public String toString() {
        return "remove " + path.getId() + " " + removeCount;
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
