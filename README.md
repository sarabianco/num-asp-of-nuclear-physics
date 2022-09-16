# Theoretical and numerical aspects of Nuclear Physics project

In this repository you can find the source code, the resulting plot and the reference to the polonium problem, plus a brief presentation of the project. The matrix exponential method is implemented on Python 3.9.4 to solve the system of Bateman equations in order to find the variation over time of the nuclides concentration. In particular the production of Polonium-210 is studied as presented in the file 'Masterproef_Maren_Vranckx.pdf'

### Repository 
Inside 'New Project' you can find different files.
The folder [src](https://github.com/sarabianco/num-asp-of-nuclear-physics/tree/main/New%20Project/src) contains the code to run. [plots](https://github.com/sarabianco/num-asp-of-nuclear-physics/tree/main/New%20Project/plots) contains the resulting plots, which you can reobtain by running the code. [Masterproef_Maren_Vranckx.pdf](https://github.com/sarabianco/num-asp-of-nuclear-physics/blob/main/New%20Project/Masterproef_Maren_Vranckx.pdf) is the reference to the Polonium problem [p. 4-6]. [Theoretical and Numerical Aspects of NP - Project.pdf](https://github.com/sarabianco/num-asp-of-nuclear-physics/blob/main/New%20Project/Theoretical%20and%20Numerical%20Aspects%20of%20NP%20-%20Project.pdf) is a brief presentation of the whole project.

### Numerical methods
The matrix exponenential method is an iterative method used to compute the solutions to the system of ODE. It computes the solution by using a constant matrix and by exponentiating it. The results are collected in an array.

### Plots
The plots show the change in nuclide concentration over time of Bi-209, Bi-210 and Po-210.

### Python libraries
The code is written on Python 3.9.4. The following libraries are used:
* numpy v. 1.22.24
* matplotlib.pyplot v. 3.4.1
* scipy v. 1.6.3
