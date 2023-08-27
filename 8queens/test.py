import random

import individual
from nQueens_GA import find_best


def create_gnome():
    return random.sample(range(0, 8), 8)

def print_result(generation, populations):
    best = find_best(populations)
    print("Generation: {}\tString: {}\tFitness: {}". \
          format(generation,
                 "".join(str(best.chromosome)),
                 str(best.f_val)))
    return best


data1 = [3, 4, 7, 1, 7, 0, 5, 4]
data2 = [8, 4, 7, 1, 7, 0, 5, 4]
test1 = individual.Individual(data1)
test2 = individual.Individual(data2)
print_result(1, [test1, test2])
