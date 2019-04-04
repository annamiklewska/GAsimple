'''
Given a target string the goal is to produce target string starting from a random string of the same length.
acceptable characters (genes):  A-Z, a-z, 0-9
'''
import random

# no of individuals in each generation:
POPULATION_SIZE = 100

# valid genes:
GENES = "abcdefghijklmnopqrstuvwxzy ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"

# target string:
TARGET = "I am the perfect string"


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.fitness_fun()  # the less the better

    @classmethod
    def mutation(cls):
        pass

    @classmethod
    def rand_gene(cls):
        global GENES
        return random.choice(GENES)

    @classmethod
    def generate_chromosome(cls):
        global TARGET
        global GENES
        length = len(TARGET)
        return [cls.rand_gene() for _ in range(length)]

    def crossover(self, partner):
        global TARGET
        child_chromosome = []
        for j, k in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(j)
            elif prob < 0.90:
                child_chromosome.append(k)
            else:
                child_chromosome.append(self.rand_gene())

        return Individual(child_chromosome)

    def fitness_fun(self):
        global TARGET
        fit = 0
        for j, k in zip(TARGET, self.chromosome):
            if j != k:
                fit += 1
        return fit


def main():
    global POPULATION_SIZE
    # current generation
    gen = 1
    print("I AM IN MAIN")

    found = False
    pop = []
    # create initial population
    for _ in range(POPULATION_SIZE):
        chromosome = Individual.generate_chromosome()
        pop.append(Individual(chromosome))

    while not found:
        # sort population in increasing order of its fitness score
        pop = sorted(pop, key=lambda x: x.fitness)
        # if the individual with the lowest fitness score == TARGET, then the goal was reached
        if pop[0].fitness <= 0:
            found = True
            break

        # otherwise generate offspring for new generation
        new_generation = []

        # elitism - 10% of the fittest individuals from old population go to new generation

        size = int(POPULATION_SIZE / 10)
        new_generation.extend(pop[:size])

        # 50% of fittest population mates to produce offspring
        size = int(POPULATION_SIZE * 9 / 10)
        half = int(POPULATION_SIZE/2)
        for _ in range(size):
            parent1 = random.choice(pop[:half])
            parent2 = random.choice(pop[:half])
            child = parent1.crossover(parent2)
            new_generation.append(child)

        pop = new_generation

        print("Generation: {}\tString: {}\tFitness: {}". \
              format(gen,
                     "".join(pop[0].chromosome),
                     pop[0].fitness))
        gen += 1

    print("Generation: {}\tString: {}\tFitness: {}". \
          format(gen,
                 "".join(pop[0].chromosome),
                 pop[0].fitness))


if __name__ == '__main__':
    main()
