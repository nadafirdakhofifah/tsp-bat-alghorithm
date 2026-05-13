import random
import numpy as np


class BatAlgorithm:
    def __init__(self, distance_matrix, population_size=20, iterations=100):
        self.distance_matrix = distance_matrix
        self.population_size = population_size
        self.iterations = iterations
        self.num_cities = len(distance_matrix)

    def generate_route(self):
        route = list(range(self.num_cities))
        random.shuffle(route)
        return route

    def fitness(self, route):
        total_distance = 0

        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[
                route[i]][route[i + 1]]

        total_distance += self.distance_matrix[
            route[-1]][route[0]]

        return total_distance

    def swap(self, route):
        new_route = route.copy()

        i, j = random.sample(range(self.num_cities), 2)

        new_route[i], new_route[j] = new_route[j], new_route[i]

        return new_route

    def optimize(self):

        bats = [self.generate_route()
                for _ in range(self.population_size)]

        best_route = min(bats, key=self.fitness)
        best_distance = self.fitness(best_route)

        history = []

        for _ in range(self.iterations):

            for i in range(self.population_size):

                new_route = self.swap(bats[i])

                if self.fitness(new_route) < self.fitness(bats[i]):
                    bats[i] = new_route

                if self.fitness(bats[i]) < best_distance:
                    best_route = bats[i]
                    best_distance = self.fitness(best_route)

            history.append(best_distance)

        return best_route, best_distance, history