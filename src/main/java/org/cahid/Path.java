package org.cahid;

import org.optaplanner.core.api.domain.entity.PlanningEntity;
import org.optaplanner.core.api.domain.lookup.PlanningId;
import org.optaplanner.core.api.domain.variable.PlanningListVariable;
import org.optaplanner.core.api.domain.variable.PlanningVariable;

import java.util.ArrayList;

@PlanningEntity
public class Path {
    @PlanningId
    private int id;

    @PlanningVariable(valueRangeProviderRefs = {"wavelengthRange"})
    private Integer wavelength;

    @PlanningListVariable(valueRangeProviderRefs = {"nodeRange"})
    private ArrayList<Integer> path;
    private int source;
    private int destination;

    public Path(){
        id = 0;
        wavelength = 0;
        path = new ArrayList<>();
        source = 0;
        destination = 0;
    }


    public Path(int id, int source, int destination) {
        this.id = id;
        this.source = source;
        this.destination = destination;
        wavelength = 0;
        path = new ArrayList<>();
        path.add(source);
    }

    public boolean isDone() {
        return path.get(path.size()-1) == destination;
    }

    // Getter and Setters
    public int getSource() {
        return source;
    }

    public void setSource(int source) {
        this.source = source;
    }

    public int getDestination() {
        return destination;
    }

    public void setDestination(int destination) {
        this.destination = destination;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getWavelength() {
        return wavelength;
    }

    public void setWavelength(int wavelength) {
        this.wavelength = wavelength;
    }

    public ArrayList<Integer> getPath() {
        return path;
    }

    public void setPath(ArrayList<Integer> path) {
        this.path = path;
    }
}
