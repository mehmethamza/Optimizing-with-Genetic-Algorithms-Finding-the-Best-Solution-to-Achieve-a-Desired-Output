Genetic Algorithm Optimization

This project uses a genetic algorithm to find the optimal set of weights for a given list of input values (function_inputs) to achieve a target output (desired_output).

Problem Description

Input Values: [4, -2, 3.5, 5, -11, -4.7]
Desired Output: 44
The goal is to find a set of weights that brings the weighted sum of these inputs as close as possible to 44.

How It Works

Initialize: Start with a population of random solutions.
Evaluate: Calculate the fitness of each solution based on how close it is to the desired output.
Select: Choose the best solutions as parents.
Crossover and Mutate: Generate new solutions by combining and modifying parents.
Repeat: Iterate through generations to find the best solution.
