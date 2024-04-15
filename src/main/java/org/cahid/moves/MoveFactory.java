package org.cahid.moves;

import org.cahid.Network;
import org.cahid.Path;
import org.optaplanner.core.impl.heuristic.move.Move;
import org.optaplanner.core.impl.heuristic.move.NoChangeMove;
import org.optaplanner.core.impl.heuristic.selector.move.factory.MoveListFactory;

import java.util.List;

public class MoveFactory implements MoveListFactory<Network> {
    @Override
    public List<? extends Move<Network>> createMoveList(Network network) {
        List<Move<Network>> moveList = new java.util.ArrayList<>();

        for (Path path: network.getPaths()) {
            if (!path.isDone()) {
                for (int neighbor: network.getTopology().get(path.getPath().get(path.getPath().size()-1))) {
                    if (path.getPath().contains(neighbor)) continue;
                    moveList.add(new ExtendPathMove(path, neighbor));
                }
            }

            for (int i = 1; i < path.getPath().size(); i++) {
                moveList.add(new RemovePathMove(path, i));
            }

            for (int i = 0; i < network.getAvailableWavelengths(); i++) {
                if (path.getWavelength() == i) continue;
                moveList.add(new ChangeWavelengthMove(path, i));
            }
        }

        return moveList;
    }


}
