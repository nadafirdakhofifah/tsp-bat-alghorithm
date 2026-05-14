import random
import numpy as np

random.seed(42)
np.random.seed(42)

from math import exp


class BatAlgorithm:

    def __init__(
        self,
        distance_matrix,
        population_size=10,
        iterations=100,
        f_min=0,
        f_max=2,
        alpha=0.9,
        gamma=0.9
    ):

        self.distance_matrix = distance_matrix
        self.population_size = population_size
        self.iterations = iterations
        self.num_cities = len(distance_matrix)

        # parameter BA
        self.f_min = f_min
        self.f_max = f_max
        self.alpha = alpha
        self.gamma = gamma

# loudness & pulse rate
        self.loudness = np.ones(population_size)
        self.pulse_rate = np.random.rand(population_size)

        # velocity & frequency
        self.velocity = np.zeros(population_size)
        self.frequency = np.zeros(population_size)

    # =====================================
    # FITNESS FUNCTION
    # =====================================

    def calculate_distance(self, route):

        total_distance = 0

        for i in range(self.num_cities - 1):

            total_distance += self.distance_matrix[
                route[i]][route[i + 1]
            ]

        # kembali ke kota awal
        total_distance += self.distance_matrix[
            route[-1]][route[0]
        ]

        return total_distance

    # =====================================
    # GENERATE RANDOM ROUTE
    # =====================================

    def generate_route(self):

        route = list(range(self.num_cities))

        random.shuffle(route)

        return route

    # =====================================
    # LOCAL SEARCH
    # =====================================

    def local_search(self, route):

        new_route = route.copy()

        city1, city2 = random.sample(
            range(self.num_cities), 2
        )

        new_route[city1], new_route[city2] = (
            new_route[city2],

            new_route[city1]
        )

        return new_route

    # =====================================
    # MAIN OPTIMIZATION
    # =====================================

    def optimize(self):

        # generate populasi awal
        bats = [
            self.generate_route()
            for _ in range(self.population_size)
        ]


        # cari best solution awal
        best_route = bats[0]
        best_distance = self.calculate_distance(best_route)

        for bat in bats:

            current_distance = self.calculate_distance(bat)

            if current_distance < best_distance:

                best_distance = current_distance
                best_route = bat.copy()

        # simpan convergence history
        history = []
        logs = []

        # =====================================
        # ITERATION
        # =====================================

        for iteration in range(self.iterations):

            for i in range(self.population_size):


                # update frequency
                beta = random.random()

                self.frequency[i] = (
                    self.f_min +
                    (self.f_max - self.f_min) * beta
                )

                # update velocity
                self.velocity[i] = (
                    self.velocity[i] +
                    (
                        self.calculate_distance(bats[i]) -
                        best_distance
                    ) * self.frequency[i]
                )

                # copy route
                new_route = bats[i].copy()

                # local search
                rand = random.random()

                if rand > self.pulse_rate[i]:


                    new_route = self.local_search(new_route)

                # hitung fitness
                new_distance = self.calculate_distance(new_route)

                current_distance = self.calculate_distance(
                    bats[i]
                )

                # accept solution
                if (
                    new_distance < current_distance
                    and
                    random.random() < self.loudness[i]
                ):

                    bats[i] = new_route.copy()

                # update global best
                if new_distance < best_distance:

                    best_distance = new_distance
                    best_route = new_route.copy()

                    log_message = (
                        f"Iterasi {iteration + 1}: "
                        f"Best Distance Update -> "
                        f"{round(best_distance, 2)}"
                    )

                    logs.append(log_message)

                # update pulse rate
                self.pulse_rate[i] = (
                    self.pulse_rate[i] *
                    (
                        1 - exp(
                            -self.gamma * iteration
                        )
                    )
                )

            history.append(best_distance)

        return best_route, best_distance, history, logs
