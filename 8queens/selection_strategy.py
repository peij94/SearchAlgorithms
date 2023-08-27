import random
import numpy.random as npr


def tournament_selection(population, num_parents, tournament_size):
    parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda pi: pi.f_val)
        parents.append(winner)
    return parents


def roulette_wheel(population, num_parents):
    max_p = sum([c.f_val for c in population])
    selection_probs = [c.f_val / max_p for c in population]
    parents = []
    for i in range(num_parents):
        random_index = npr.choice(len(population), p=selection_probs)
        parents.append(population[random_index])
    return parents


def stochastic_universal_sampling(population, num_parents):
    total_fitness = sum(pi.f_val for pi in population)
    selection_pointer_distance = total_fitness / num_parents

    start_point = random.uniform(0, selection_pointer_distance)
    pointers = [start_point + i * selection_pointer_distance for i in range(num_parents)]

    parents = []
    cumulative_fitness = 0
    current_parent_index = 0

    for pi in population:
        cumulative_fitness += pi.f_val

        while cumulative_fitness > pointers[current_parent_index]:
            parents.append(pi)
            current_parent_index += 1

            if current_parent_index >= num_parents:
                return parents
    return parents
