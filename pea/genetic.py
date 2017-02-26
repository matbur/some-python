import random

from graph import Graph


class Genetic:
    def __init__(self, graph):
        self.graph = graph
        self.problem_size = graph.get_dim()

        self.number_of_iterations = 5000
        self.mutation_probability = .05
        self.cross_probability = .60

        self.path = list(range(self.problem_size))

        self.population = []

        self.initialize()

    def run(self):
        population = self.population
        fitness = self.fitness

        best_order = population[0]
        best_fitness = fitness(best_order)

        i = 0
        while i < self.number_of_iterations:
            i += 1
            a = random.choice(population)
            af = fitness(a)
            b = random.choice(population)
            bf = fitness(b)

            c = self.probably_cross([a, b])
            self.probably_mutate(c)

            fitness1 = fitness(c)
            if fitness1 < best_fitness:
                i = 0
                print('ok', fitness1, best_fitness)
                best_order = c
                best_fitness = fitness1
            else:
                print('nie ok', fitness1, best_fitness)

            if fitness1 < af:
                population[population.index(a)] = c
            elif fitness1 < bf:
                population[population.index(b)] = c

        return self.get_path(best_order), best_fitness

    def initialize(self):
        problem_size = self.problem_size
        for _ in range(problem_size):
            r = [random.randrange(problem_size // 2)
                 for _ in range(problem_size)]
            self.population.append(r)

    def get_path(self, order):
        temp_path = self.path[:]
        result_path = []
        order_iter = iter(order)
        while temp_path:
            order_next = min(next(order_iter), len(temp_path) - 1)
            # print(temp_path, order_next, result_path)
            result_path.append(temp_path.pop(order_next))

        return result_path

    def get_total_weight(self, order):
        return self.graph.get_path_weight(self.get_path(order))

    def fitness(self, order):
        path = self.get_path(order)
        return self.graph.get_path_weight(path)

    def mutate(self, order):
        x, y = self.random_different()
        order[x] = y // 2

    def probably_mutate(self, order):
        probability = self.mutation_probability
        if random.random() < probability:
            self.mutate(order)

    def cross(self, orders):
        x, y = self.random_different()
        random.shuffle(orders)
        l1, l2 = orders

        return l1[:x] + l2[x:y] + l1[y:]

    def probably_cross(self, orders):
        probability = self.cross_probability
        if random.random() < probability:
            return self.cross(orders)
        return orders[random.randrange(2)]

    def random_different(self):
        size = self.problem_size

        x = random.randrange(size)
        y = random.randrange(size)
        while x == y:
            y = random.randrange(size)

        return sorted([x, y])


if __name__ == '__main__':
    # graph = Graph.from_file('br17.atsp')
    graph = Graph.from_file('data/atsp/ft53.atsp')
    # import sys
    #
    # graph = Graph.from_file(sys.argv[1])
    # print(graph)
    gen = Genetic(graph)
    best = gen.run()
    print(best)
