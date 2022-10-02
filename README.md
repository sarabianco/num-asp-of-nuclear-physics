# Theoretical and numerical aspects of Nuclear Physics project

In this repository you can find the source code of a Bateman solver. Any system of Bateman Equation can potentially be solved using this code. As an example, you can find the resulting plot and the reference to the polonium problem, plus a brief presentation of the project. The matrix exponential method is implemented on Python 3.9.4 to solve the system of Bateman equations in order to find the variation over time of the nuclides concentration. In particular the production of Polonium-210 is studied as presented in the file 'Masterproef_Maren_Vranckx.pdf'

### Repository 
```
.
├── Polonium Project                     
|   ├── plots                                                   # Resulting plots
|   |   ├── Bismuth-209 concentration.png
|   |   ├── Bismuth-210 concentration.png
|   |   ├── Polonium-210 concentration.png
|   ├── src
|   |   ├── bateman_solver.py                                   # Code to run
|   ├── data
|   |   ├── Polonium_problem.txt                                # Input .txt file containing the data for the Polonium Problem
|   ├── results
|   |   ├── Polonium_results.txt                                # Output .txt file containing the results to the Polonium Problem
|   ├── Masterproef_Maren_Vranckx.pdf                           # Reference to the project
|   ├── Theoretical and Numerical Aspects of NP - Project.pdf   # Presentation of the project
└── README.md
```

### Usage
In order to use the code, simply open a terminal in the correspondent working directory and run:
```
$ python Polonium_problem_project.py
```
By launching the .py file, an output file to visualize the solutions will be automatically created and saved into `results`. Plots will be shown on screen and the user can save them. The user is asked to answer some questions that will appear on the terminal.
In `data` you have to put the data of the problem using the following format

```
T = value
initial_values = [value0, value1, .., valuen]
bateman_matrix = [value00, value01, .., value0n; value10, value11, .., value1n; ..; valuen0, valuen1, .., valuenn]
```
In particular, *T* is the time of the simulation, *initial_values* is an array containing the initial values of the nuclides in the system of Bateman equation and *bateman_matrix* is the Bateman matrix of the problem.
The folder `data` contains an example of the input file.

### Numerical methods
The matrix exponenential method is an iterative method used to compute the solutions to the system of ODE. It computes the solution by using a constant matrix and by exponentiating it. The results are collected in an array. Python uses the function 'scipy.linalg.expm' which is essentially a Pade approximation with a variable order that is decided based on the array data.

### Plots
The plots show the change in nuclide concentration over time of Bi-209, Bi-210 and Po-210.

### Python libraries
The code is written on Python 3.9.4. The following libraries are used:
* numpy v. 1.22.24
* matplotlib.pyplot v. 3.4.1
* scipy v. 1.6.3
