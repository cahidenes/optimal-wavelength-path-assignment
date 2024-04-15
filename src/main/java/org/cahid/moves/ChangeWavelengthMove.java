package org.cahid.moves;

import org.cahid.Network;
import org.cahid.Path;
import org.optaplanner.core.api.score.director.ScoreDirector;
import org.optaplanner.core.impl.heuristic.move.AbstractMove;

import java.util.Collection;
import java.util.Collections;

public class ChangeWavelengthMove extends AbstractMove<Network> {
    Path path;
    int newWavelength;
    int oldWavelength;

    public ChangeWavelengthMove(Path path, int newWavelength) {
        this.path = path;
        this.newWavelength = newWavelength;
        this.oldWavelength = path.getWavelength();
    }

    @Override
    protected AbstractMove<Network> createUndoMove(ScoreDirector<Network> scoreDirector) {
        return new ChangeWavelengthMove(path, oldWavelength);
    }

    @Override
    protected void doMoveOnGenuineVariables(ScoreDirector<Network> scoreDirector) {
        scoreDirector.beforeVariableChanged(path, "path");
        path.setWavelength(newWavelength);
        scoreDirector.afterVariableChanged(path, "path");
        scoreDirector.triggerVariableListeners();
    }

    @Override
    public boolean isMoveDoable(ScoreDirector<Network> scoreDirector) {
        return true;
    }

    @Override
    public String getSimpleMoveTypeDescription() {
        return "Change wavelength of path " + path.getId() + " to " + newWavelength;
    }

    @Override
    public String toString() {
        return "change " + path.getId() + " " + newWavelength;
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
