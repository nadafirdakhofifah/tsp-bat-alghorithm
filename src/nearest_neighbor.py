import numpy as np

class NearestNeighbor:

    def __init__(self, distance_matrix):

        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    # =====================================
    # HITUNG TOTAL DISTANCE
    # =====================================

    def calculate_distance(self, route):

        total_distance = 0

        for i in range(len(route) - 1):

            total_distance += self.distance_matrix[
                route[i]
            ][
                route[i + 1]
            ]

        # kembali ke kota awal
        total_distance += self.distance_matrix[
            route[-1]
        ][
            route[0]
        ]

        return total_distance

    # =====================================
    # NEAREST NEIGHBOR PROCESS
    # =====================================

    def optimize(self):

        unvisited = list(range(self.num_cities))

        current_city = 0

        route = [current_city]

        unvisited.remove(current_city)

        logs = []

        iteration = 1

        while unvisited:

            nearest_city = min(
                unvisited,
                key=lambda city:
                self.distance_matrix[current_city][city]
            )

            route.append(nearest_city)

            current_distance = self.calculate_distance(route)

            log_message = (
                f"Iterasi {iteration}: "
                f"Kota {nearest_city} dipilih -> "
                f"Distance = {round(current_distance, 2)}"
            )

            logs.append(log_message)

            current_city = nearest_city

            unvisited.remove(nearest_city)

            iteration += 1

        total_distance = self.calculate_distance(route)

        history = []

        cumulative_distance = 0

        for i in range(len(route) - 1):

            cumulative_distance += self.distance_matrix[
                route[i]
            ][
                route[i + 1]
            ]

            history.append(cumulative_distance)

        return route, total_distance, history, logs