# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:35:43 2016

@author: Administrator
"""

import pylab as pl
import math
class nuclei_decay:
    """
    Simulation of a decay problem with two types of nuclei
    Program to solve Chapter 1 Exercise *1.5. of 'Computational Physics' by Prof. Cai
    """
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 0.5, time_of_duration = 5, time_step1 = 0.05, time_step2 = 0.1 ):
        self.n_A1 = [number_of_nuclei_A]
        self.n_B1 = [number_of_nuclei_B]
        self.n_A2 = [number_of_nuclei_A]
        self.n_B2 = [number_of_nuclei_B]
        self.n_A1_true = [number_of_nuclei_A]
        self.n_B1_true = [number_of_nuclei_B]
        self.n_A2_true = [number_of_nuclei_A]
        self.n_B2_true = [number_of_nuclei_B]
        self.N = number_of_nuclei_A + number_of_nuclei_B
        self.t1 = [0]
        self.t2 = [0]
        self.tau = time_constant
        self.dt1 = time_step1
        self.dt2 = time_step2
        self.time = time_of_duration
        self.nsteps1 = int(time_of_duration // time_step1 + 1)
        self.nsteps2 = int(time_of_duration // time_step2 + 1)
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("Time step1 ->", time_step1)
        print("Time step2 ->", time_step2)
        print("Total time ->", time_of_duration)

    def calculate(self):
        for i in range(self.nsteps1):
            tmp_A1 = self.n_A1[i] + (self.N - 2 * self.n_A1[i]) / self.tau * self.dt1
            tmp_B1 = self.N - tmp_A1
            self.n_A1.append(tmp_A1)
            self.n_B1.append(tmp_B1)
            self.t1.append(self.t1[i] + self.dt1)
            tmp_A1_true = self.N / 2 - math.exp(- 2 * self.t1[i + 1] / self.tau) * (self.N - 2 * self.n_A1_true[0]) / 2 
            tmp_B1_true = self.N - tmp_A1_true
            self.n_A1_true.append(tmp_A1_true)
            self.n_B1_true.append(tmp_B1_true)
        for i in range(self.nsteps2):
            tmp_A2 = self.n_A2[i] + (self.N - 2 * self.n_A2[i]) / self.tau * self.dt2
            tmp_B2 = self.N - tmp_A2
            self.n_A2.append(tmp_A2)
            self.n_B2.append(tmp_B2)
            self.t2.append(self.t2[i] + self.dt2)
            tmp_A2_true = self.N / 2 - math.exp(- 2 * self.t2[i + 1] / self.tau) * (self.N - 2 * self.n_A2_true[0]) / 2 
            tmp_B2_true = self.N - tmp_A2_true
            self.n_A2_true.append(tmp_A2_true)
            self.n_B2_true.append(tmp_B2_true)
           
    def show_results(self):
        pl.plot(self.t1, self.n_A1, 'b--', label='A1: Time Step = 0.05')
        pl.plot(self.t1, self.n_B1, 'b', label='B1: Time Step = 0.05')
        pl.plot(self.t2, self.n_A2, 'g--', label='A2: Time Step = 0.1')
        pl.plot(self.t2, self.n_B2, 'g', label='B2: Time Step = 0.1')
        pl.plot(self.t1, self.n_A1_true, 'r--', label='True A1: Time Step = 0.05')
        pl.plot(self.t1, self.n_B1_true, 'r', label='True B1: Time Step = 0.05')
        pl.plot(self.t2, self.n_A2_true, 'c--', label='True A2: Time Step = 0.1')
        pl.plot(self.t2, self.n_B2_true, 'c', label='True B2: Time Step = 0.1')
        pl.title('Double Decay Probelm-Approximation Compared with True in Defferent Time Steps')
        pl.xlim(0.0, 0.1)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='best', shadow=True, fontsize='small')
        pl.grid(True)
        pl.savefig("computational_physics homework 4(improved-7).png")
        
    def store_results(self):
        myfile = open('computational_physics homework 4(improved-7) data.txt', 'w')
        for i in range(len(self.t1)):
            print(self.t1[i], self.n_A1[i], self.n_B1[i], self.n_A1_true[i], self.n_B1_true[i], file = myfile)
        for i in range(len(self.t2)):
            print(self.t2[i], self.n_A2[i], self.n_B2[i], self.n_A2_true[i], self.n_B2_true[i], file = myfile)
        myfile.close()

#matplotlib inline
a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()
        
        