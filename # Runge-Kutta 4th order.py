
#The first method which is tried to solve the Bateman's equation is the RK4. We deal with a system of ODE which have
#been simplified considering some approximation in the parameters used in the eqs. The simpler version of Euler's method
#is tried and then matrix manipulation. For the different methods, the error is then plotted to understand which method
#is the best for this problem.

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
     
def rk4_method(f,U_0,dt,T,N_t):
    # Ensure that any list/tuple returned from f_ is wrapped as array
    f_ = lambda u: asarray(f(u))
    u = np.zeros((T+1 , len(U_0)))
    '''k1 = np.zeros((1, len(U_0)))
    k2 = np.zeros((1, len(U_0)))
    k3 = np.zeros((1, len(U_0)))
    k4 = np.zeros((1, len(U_0)))'''
    t = linspace(0, T, 1)

    u[0] = U_0
    for i in range(T): 
        k1 = dt*f_(u[i])
        k2 = dt*f_(u[i]+k1/2)
        k3 = dt*f_(u[i]+k2/2)
        k4 = dt*f_(u[i]+k3)
        u[i+1] = u[i]+(k1+2*k2+2*k3+k4)/6
    print(u)
    return u
        
def euler_method(f, U_0, dt, T):
    N_t = int(round(float(T)/dt)) #number of steps
    # Ensure that any list/tuple returned from f_ is wrapped as array
    f_ = lambda u: asarray(f(u))
    u = np.zeros((T+1, len(U_0)))
    t = linspace(0, T, 1)
    u[0] = U_0
    for n in range(T): # N_t
        u[n+1] = u[n] + dt*f_(u[n])
    return u

def test_bateman():
    """Test case using a SIR model."""
    gamma_I = 0.061; gamma_X = 0.003; lam_I = 2.874e-5; lam_X = 2.027e-5; sig_aX = 2.75e-18; nu = 2.3
    phi = 4.42e16; sigma_f = 0.008

    def f(u):
        I, X = u
        return [gamma_I * sigma_f * 0 - lam_I*I, gamma_X * sigma_f * 0 + gamma_I*I - lam_X * X - sig_aX * X * 0]

    #computing in hours
    dt = 3600 #time steps
    #N_t = 70 # no of hours
    T = 70 #dt*N_t # End time
    N_t = int(round(float(T))/dt)
    I_0 = (gamma_I * sigma_f * phi)/ lam_I
    #X_0 = (gamma_X + sigma_f * phi + lam_I * I_0) / (lam_X + sig_aX * phi)
    X_0 = sigma_f * phi * (gamma_I + gamma_X) / (lam_X + sig_aX * phi)
    U_0 = [I_0, X_0]
    print(U_0)

    #u = rk4_method(f, U_0, dt, T, N_t)
    u = euler_method(f, U_0, dt, T)

    I = u[:,0]
    X = u[:,1]
    
    rho = (sig_aX*X)/(nu * sigma_f)

    fig = plt.figure()
    '''l1, l2 = plt.plot(t, I, t, X)
    fig.legend((l1, l2), ('I', 'X'), 'lower right')'''
    l1= plt.plot(rho, '-ro')
    fig.legend((l1), ('rho'), 'lower right')
    plt.xlabel('hours')
    plt.show()

    # Consistency check:
    '''N = S[0] + I[0] + R[0]
    eps = 1E-12 # Tolerance for comparing real numbers
    for n in range(len(S)):
        SIR_sum = S[n] + I[n] + R[n]
    if abs(SIR_sum - N) > eps:
        print('consistency check failed: S+I+R='+ SIR_sum + ' !='+ N )'''

if __name__ == '__main__':
    test_bateman()
