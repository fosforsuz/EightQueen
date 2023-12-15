import random

board_size = 8

def calculate_fitness(chromosome):
    clashes = 0
    for i in range(len(chromosome)):
        for j in range(i+1, len(chromosome)):
            if chromosome[i] == chromosome[j] or abs(i - j) == abs(chromosome[i] - chromosome[j]):
                clashes += 1
    return 28 - clashes

def create_initial_population(population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(board_size))
        random.shuffle(individual)
        population.append(individual)
    return population

def tournament_selection(population, fitness_scores, tournament_size):
    selected = []
    for _ in range(len(population)):
        participants = random.choices(range(len(population)), k=tournament_size)  # Convert participants to a list of indices
        participants_fitness = [(i, fitness_scores[idx]) for i, idx in enumerate(participants)]  # Use enumerate to get the index and fitness score
        winner = max(participants_fitness, key=lambda x: x[1])
        selected.append(population[winner[0]])
    return selected

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, board_size - 1)
    parent1_set = set(parent1[:crossover_point])
    child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1_set]
    parent2_set = set(parent2[:crossover_point])
    child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2_set]
    return child1, child2

def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(board_size), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def print_board(solution):
    for row in range(board_size):
        line = ""
        for col in range(board_size):
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def genetic_algorithm(population_size, mutation_rate, generations):
    population = create_initial_population(population_size)
    best_solution = None
    for generation in range(generations):
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
        new_population = []
        while len(new_population) < population_size:
            selected = tournament_selection(population, fitness_scores, 3)
            parent1, parent2 = random.sample(selected, 2)
            offspring1, offspring2 = single_point_crossover(parent1, parent2)
            offspring1 = mutation(offspring1, mutation_rate)
            offspring2 = mutation(offspring2, mutation_rate)
            new_population.extend([offspring1, offspring2])
        population = new_population
        current_best_solution = max(population, key=lambda x: calculate_fitness(x))
        if best_solution is None or calculate_fitness(current_best_solution) > calculate_fitness(best_solution):
            best_solution = current_best_solution
            if calculate_fitness(best_solution) == 28:
                break
    print_board(best_solution)
    return best_solution, generation

solution, generation = genetic_algorithm(population_size=100, mutation_rate=0.2, generations=1000)
print("En iyi çözüm:", solution, "Generation:", generation)
