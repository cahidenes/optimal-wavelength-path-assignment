# Optimal Wavelength Path Assignment Algorithm

This repository contains the source code of Optimal Wavelength Path Assignment Algorithm using Strategic Oscillation Local Search.

## Source Code

The source code can be found in the `src` folder. Used optimization library, Optaplanner, can be checked [here](https://www.optaplanner.org/)

## Executable

The `build` folder contains a jar file that you can run with the following command:
```bash
java -jar build/solver.jar <input_file>
```

The `tests` folder contains some sample input files that are used for testing purposes. You can use these files while running the executable.

## Python Scripts

The `python-scripts` folder contains some scripts that are used in the project.

- `generate_input.py` script is used for generating random inputs.
- `linear_programming.py` file contains implementations of integer programming that solves the optimal wavelength path assignment problem optimally. The file also contains the relaxation of the integer programming which outputs an upper bound for the optimal solution.

## Presentation

The presentation is prepared using `manim-community` and `manim-slides`. Manim is a perfect tool for animating math related content using Python. Manim-slides converts manim animations into presentations.

`presentation` folder contains python code which is used to prepare the presentaion. To generate animations, use the following command:
```bash
# To generate low quality videos:
manim -pql main.py <list of sections>

# To generate high quality videos:
manim -pqh main.py <list of sections>
```

Sections include
- Intro
- WDM
- Problem
- Solution
- Recap
- Moves
- Score
- OptimizationMethod
- Tests
- Conclusion

Also compiled videos can be found in the `presentation.zip` file.

## Project Report

You can read the project report from the `Project Report.pdf` file.
