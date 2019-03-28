'''
Given a target string the goal is to produce target string starting from a random string of the same length.
acceptable characters (genes):  A-Z, a-z, 0-9
'''
import random

import numpy as np

# no of individuals in each generation:
population_size = 50

# valid genes:
GENES = "abcdefghijklmnopqrstuvwxzy ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"

# target string:
TARGET = "I am the perfect string"

class Individual:
    def __init__(self, str):
        self.str = str
        self.fitness = self.fitness_fun() # the less the better

    @classmethod
    def mutation(cls):
        pass

    @classmethod
    def generate_str(cls):
        global TARGET
        global GENES
        return ''.join(random.choice(GENES) for i in range(len(TARGET)))

    def crossover(self, partner):
        global TARGET
        k = len(TARGET)
        child = self.str
        pass

    def fitness_fun(self):
        global TARGET
        fit = 0
        for j, k in zip(TARGET, self.str):
            if j != k:
                fit += 1
        return fit

def main():
    pass
