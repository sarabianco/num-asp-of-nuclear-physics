import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import linalg
import csv

#===================================== Matrix Exponential Method implementation ====================================

def matrix_exponential_method(U_0,dt,T,A):
    '''
    U_0 = (array) initial values of ODE system's functions

    dt = (int) number of points in each step

    T = (int) number of steps

    A = (array) square matrix containing the coefficients of the ODE system

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

#=========================================== Read File  ====================================================

def readfile(filename):
    '''
    filename = (str) Input the name of the file
    '''
    # Open file
    file = open(filename, 'r')

    # Read file lines
    lines = file.readlines()

    def create_init_values(x):
        x = x.split('=')[1]
        x = x.split('[')[1]
        x = x.split(']')[0]
        x = x.split(',')
        return np.array([float(n) for n in x])

    def create_matrix(x):
        matrix = []
        x = x.split('=')[1]
        x = x.split('[')[1]
        x = x.split(']')[0]
        x = x.split(';')
        for i in range(len(x)):
            y = x[i].split(',')
            matrix.append([float(n) for n in y])
        return np.array(matrix)

    # Read time T, the initial nuclide concentration array and the Bateman matrix
    T = int((lines[0].split('=')[1])) 
    init_values = create_init_values(lines[1])
    bateman_matrix = create_matrix(lines[2])
    
    # Close file
    file.close()

    return T, init_values, bateman_matrix

#=========================================== Write File  ====================================================

def write_file(filename, columns, rows, file_content):
    '''
    filename = (str) Name of the file

    columns = (int) Number of columns in the file

    rows = (int) Number of rows in the file

    file_content = (array) Matrix you want to write on the file
    '''
    # Open file
    file = open("../results/" + filename, 'w')
    writer = csv.writer(file)

    # Create first row with columns titles
    line = ['T']

    for i in range(columns):
        print("Insert title column", i+1,". Note that column", i+1, " is the solution to equation", i+1, "of the Bateman system.")
        name = str(input())
        line.append("%s" % name) 

    writer.writerow(line)       

    # Fill file with results
    for i in range(rows):
        line = [i,file_content[i,:]]
        writer.writerow(line)

    # Close file
    file.close()

#=========================================== Results and Plots  ====================================================

def plot(i,limit,y,xlab,ylab,title, y_min=None,y_max=None,xmin = None,xmax=None):
    '''
    i = (int) input different int number to plot on different canvas
    
    y = (array) plot y using x as index array 0..N-1, where N is the dimension of y

    xlab = (string) label on x axis

    ylab = (string) label on y axis

    title = (string) figure title

    y_min = (int) lower limit for the y axis. The default is None

    y_max = (int) upper limit for the y axis. The default is None
    
    x_min = (int) lower limit for the x axis. The default is None

    x_max = (int) lower limit for the x axis. The default is None

    '''
    plt.figure(i)

    if (limit=="Yes"):
        plt.ylim(y_min,y_max)
        plt.xlim(xmin, xmax)

    plt.plot(y, '#000080')
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.ticklabel_format(axis = "y", style = "sci", scilimits=(0,0))
    plt.tick_params('both', direction = 'in')
    
#================================================== Bateman solver ===============================================

def bateman_solver():

    print("Insert the name of the .txt data file with the extension")
    filename = str(input())
    T, init_values, bateman_matrix = readfile("../data/" + filename)
    
    # Counts number of elements of the initial values array to get the total number equation in the Bateman system
    dimension_bateman_sys = len(init_values)

    # Time unit: 1 day
    dt = 60*60*24 # seconds in a day
    
    # Compute the solution to the Bateman's system
    bateman_sol = matrix_exponential_method(init_values,dt,T,bateman_matrix)

    # Create a file with the results
    print("Do you wish to save the results on an external .txt file? [Yes/No]")
    save = str(input())
    if (save != "Yes" and save != "No"):
        print("Please write only 'Yes' or 'No' (first letter must be uppercase)")
        save = str(input())

    if (save == "Yes"):
        # Create a new .txt file 
        print("How do you want to name your .txt file? Write also the extension")
        fname = str(input())

        # Write results
        print ("Writing results to %s.." % fname)
        write_file(fname, dimension_bateman_sys, T, bateman_sol)
        print("Done!")

    # Plots
    print("Input the label of the x axis of the plot")
    xlabel = str(input())
    print("Input the label of the y axis of the plot")
    ylabel = str(input())
 
    for i in range(dimension_bateman_sys):

        print("Input the title of plot",  i+1)
        title = str(input())
        print("Do you wish to put limits on the y and x axis? [Yes/No]")
        limit = str(input())

        if (limit != "Yes" and limit != "No"):
            print("Please write only 'Yes' or 'No' (first letter must be uppercase)")
            limit = str(input())

        if (limit == "Yes"):
            print("Insert the lower y limit")
            ymin = float(input())
            print("Insert the upper y limit")
            ymax = float(input())
            print("Insert the lower x limit")
            xmin = float(input())
            print("Insert the upper x limit")
            xmax = float(input())
            plot(i,limit, bateman_sol[:,i], xlabel, ylabel, title, ymin, ymax, xmin, xmax)

        else: 
            plot(i,limit, bateman_sol[:,i], xlabel, ylabel, title)

    plt.show()    

if __name__ == '__main__':
    bateman_solver()