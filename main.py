import pygad
import numpy

# Input variables and desired output
function_inputs = [4, -2, 3.5, 5, -11, -4.7] 
desired_output = 44 

# Fitness function to evaluate each solution
def fitness_func(solution, solution_idx):
    output = numpy.sum(solution * function_inputs)
    fitness = 1.0 / numpy.abs(output - desired_output)
    return fitness

fitness_function = fitness_func

# Parameters for the Genetic Algorithm
num_generations = 100 
num_parents_mating = 7
sol_per_pop = 50
num_genes = len(function_inputs)

# Variable to track fitness changes
last_fitness = 0

# Callback function to summarize each generation
def generation_summary(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness = {fitness}".format(fitness=ga_instance.best_solution()[1]))
    print("Change = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))
    last_fitness = ga_instance.best_solution()[1]

# Create an instance of the Genetic Algorithm
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       on_generation=generation_summary)

# Run the Genetic Algorithm
ga_instance.run()

# Retrieve and print the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Best solution variable values: {solution}".format(solution=solution))
print("Index of the individual that gives the best solution: {solution_idx}".format(solution_idx=solution_idx))

# Predict output using the best solution
prediction = numpy.sum(numpy.array(function_inputs) * solution)
print("Output with the best solution: {prediction}".format(prediction=prediction))

# Check which generation the best solution was obtained
if ga_instance.best_solution_generation != -1:
    print("Best solution obtained after {best_solution_generation} generations."
          .format(best_solution_generation=ga_instance.best_solution_generation))
