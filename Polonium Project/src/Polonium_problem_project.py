import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import scipy as sp
from scipy import linalg
from tabulate import tabulate

#===================================== Matrix Exponential Method implementation ====================================

def matrix_exponential_method(U_0,dt,T,A):
    '''
    U_0 = (array) initial values of ODE system's functions

    dt = (int) number of points in each step

    T = (int) number of steps

    A = (array) coefficients' matrix of the ODE system

    Returns a matrix in which each column contains the points solution to a different function of the ODE system
    '''

    # Definition of u matrix
    u = np.zeros((T+1, len(U_0)))

    # Fill u with initial values
    u[0] = U_0

    # Iteration
    for i in range(T):
        u[i+1] = linalg.expm((dt*A)).dot(u[i])

    return u

def print_results(T, Bi209, Bi210, Po210):
        #Print the results
    table = []

    for i in range(T):
        table.append([i, Bi209[i], Bi210[i], Po210[i]])
    
    print("Results")
    print(" ")
    print(tabulate(table, headers=['t', 'Bismuth-209', 'Bismuth-210', 'Polonium-210']))
    print(" ")

def plot(i,y_min,y_max,y,title):
    plt.figure(i)
    plt.ylim(y_min,y_max)
    plt.xlim(0, 400)
    plt.plot(y, '#000080')
    plt.title(title)
    plt.xlabel('Time (days)')
    plt.ylabel('Nuclide concentration')
    plt.ticklabel_format(axis = "y", style = "sci", scilimits=(0,0))
    plt.tick_params('both', direction = 'in')
    
#================================================ The Polonium Problem =============================================

def polonium_problem():

    # Decay constants of the nuclides
    lambdaBi_209 = 1.83163e-12
    lambdaBi_210 = 1.60035e-6
    lambdaPo_210 = 5.79764e-8

    # Time unit: 1 day
    T = 365 # Simulate for one year (365 days)
    dt = 60*60*24 # seconds in a day
    
    # Initial concentration of the different nuclides
    Bi209_0 = 6.95896e-4
    Bi210_0 = 0
    Po210_0 = 0
    init_value = [Bi209_0, Bi210_0, Po210_0]

    # Bateman Matrix 
    A = np.array([[-lambdaBi_209, 0, 0],
                  [lambdaBi_209, -lambdaBi_210, 0],
                  [0, lambdaBi_210, -lambdaPo_210]])

    # Compute the solution to the Bateman's system
    bateman_sol = matrix_exponential_method(init_value,dt,T,A)
 
    Bi209 = bateman_sol[:,0]
    Bi210 = bateman_sol[:,1]
    Po210 = bateman_sol[:,2]

    #Print results
    print_results(T, Bi209, Bi210, Po210)

    # Plots 
    plot(0,69580.0e-8,69600.0e-8,Bi209,'Bismuth-209 concentration')
    plot(1,0,8.5e-10,Bi210,'Bismuth-210 concentration')
    plot(2,0,2e-8,Po210,'Polonium-210 concentration')

    plt.show()

if __name__ == '__main__':
    polonium_problem()