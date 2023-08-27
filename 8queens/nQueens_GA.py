import random
import time

import individual
from selection_strategy import stochastic_universal_sampling, roulette_wheel, tournament_selection

solutions = set()
threshold = 92  # number of solutions
t_limit = 300  # time limit


def print_solutions(populations):
    populations = list(populations)
    # print solution's chromosomes, 10 each line
    print("Number of solutions: ", len(populations))
    for i in range(len(populations)):
        print(populations[i].chromosome, end="\t")
        if (i + 1) % 5 == 0:
            print()


def find_best(populations):
    # for all its element that f_val is the minimum
    fittest = []
    for population in populations:
        if population.f_val == 0:
            fittest.append(population)
    return list(dict.fromkeys(fittest))


def print_result(generation, populations):
    # print all solutions in current generation takes time, just print numbers here.
    print("Generation: {}\tCurrent generation solutions: {}\t".format(str(generation), str(len(populations))))


# n is the number of individuals in the population; x is the fraction of the population to be replaced by crossover in
# each iteration; and u is the mutation rate.
def solver(n, x, u):
    # Initialise generation 0
    # initial population
    p = []
    k = 0
    Ta = time.time()
    for i in range(n):
        p.append(individual.Individual(individual.create_gnome()))
    solutions.update(find_best(p))
    p_next = []
    time_consumed = 0
    while len(solutions) < threshold and time_consumed < t_limit:
        # create generation k + 1:
        base = p if k == 0 else p_next
        # 1. Copy
        p_next.extend(random.sample(base, int((1 - x) * n)))
        # 2. Crossover
        # there could be different parent selection strategies
        parents = stochastic_universal_sampling(base, int(x * n))
        # parents = roulette_wheel(base, int(x * n))
        # parents = tournament_selection(base, int(x * n), 3)
        children = []
        for i in range(0, len(parents), 2):
            first = parents[i]
            second = parents[i + 1] if i + 1 < len(parents) else None
            children = individual.cross_over(first, second)
        # get sublist of children that are valid
        valid_children = list(filter(lambda obj: individual.is_valid(obj.chromosome), children))
        # get the list of children reduce valid_children
        invalid_children = list(filter(lambda obj: not individual.is_valid(obj.chromosome), children))
        p_next.extend(valid_children)
        # 3. Mutate
        for i in range(len(invalid_children)):
            child = individual.mutated_genes(invalid_children[i], randomly=False)
            p_next.append(child)
        # Evaluate p_next
        fittest = find_best(p_next)  # fittest population of current generation
        print_result(k, fittest)
        solutions.update(fittest)
        k += 1
        Tb = time.time()
        time_consumed = Tb - Ta


T1 = time.time()
solver(100, 0.6, 0.1)
T2 = time.time()
total_time = T2 - T1
print("Time cost: ", total_time)
print_solutions(solutions)
