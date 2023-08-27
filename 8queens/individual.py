import random


def create_gnome():
    return random.sample(range(0, 8), 8)


def count_duplicates(numbers):
    duplicates = 0
    seen = set()

    for num in numbers:
        if num in seen:
            duplicates += 1
        else:
            seen.add(num)

    return duplicates


def make_it_valid(individual):
    lst = individual.chromosome
    seen = set()
    duplicated = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
        else:
            duplicated.add(num)
    # list lst reduce list of set seen
    choices = list(set(range(0, 8)) - seen)
    for duplicated_value in list(duplicated):
        choice = random.choice(choices)
        lst[lst.index(duplicated_value)] = choice
        choices.remove(choice)
    return Individual(lst)


def cross_over(parent1, parent2):
    lst1 = parent1.chromosome
    lst2 = parent2.chromosome
    # assume random cross over point
    crossover_point = random.randint(0, 7)
    child1 = lst1[:crossover_point] + lst2[crossover_point:]
    child2 = lst2[:crossover_point] + lst1[crossover_point:]
    return Individual(child1), Individual(child2)


def mutated_genes(individual, randomly=True):
    # randomly = True randomly mutated, otherwise, compulsory make the mutated gene valid.
    lst = individual.chromosome
    if randomly:
        mutated_index = random.randint(0, len(lst) - 1)
        mutated_value = random.randint(0, 7)
        lst[mutated_index] = mutated_value
    else:
        make_it_valid(individual)
    return Individual(lst)


def is_valid(lst):
    return count_duplicates(lst) == 0


class Individual:
    # an example possible solution (chromosome) is represented as list [0, 8): e.g. [0,1,2,3,4,5,6,7]

    def __init__(self, lst):
        self.chromosome = lst
        self.f_val = self.cal_fitness()

    def cal_fitness(self):
        chromosomes = self.chromosome
        total_conflicts = 0
        row = 0
        # check vertical
        total_conflicts += count_duplicates(chromosomes)
        # check diagonal
        size = len(chromosomes)
        base_list = list(range(size))  # return a list range from 0 to size
        for i in range(size):
            diagonal = [num - i for num in base_list]
            for x in diagonal:
                if x != 0 and chromosomes[i + x] == chromosomes[i] + x:
                    total_conflicts += 1
        return total_conflicts
