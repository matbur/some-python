#!/usr/bin/env python3

import copy
import random

from graph import Graph


class TabuSearch:
    def __init__(self, graph, tabu_list):
        self.graph = graph
        self.tabu_list = tabu_list

        self.current_solution = []
        self.number_of_iterations = graph.get_dim() * graph.get_dim() * 10
        self.problem_size = graph.get_dim()

        self.best_solution = []
        self.best_cost = 0
        self.no_improvement = 0

        self.setup_current_solution()
        self.setup_best_solution()

    def setup_current_solution(self):
        self.current_solution = list(range(self.problem_size))

    def setup_best_solution(self):
        self.best_solution = copy.deepcopy(self.current_solution)
        self.best_cost = self.graph.get_path_weight(self.best_solution)

    def restart(self):
        sol = copy.copy(self.current_solution)
        sol.pop(0)
        random.shuffle(sol)
        sol.insert(0, 0)
        current_cost = self.graph.get_path_weight(sol)
        if current_cost < self.best_cost:
            self.best_solution = copy.deepcopy(self.current_solution)
            self.best_cost = current_cost

    def run(self):
        for i in range(self.number_of_iterations):
            # print(i, self.no_improvement)
            self.step()

            if self.no_improvement >= self.problem_size * 10:
                self.restart()
                self.no_improvement = 0

        print('best cost', self.best_cost)
        print('solution', self.current_solution)

    def step(self):
        j = random.randrange(1, self.problem_size)
        k = random.randrange(1, self.problem_size)
        while j == k:
            k = random.randrange(1, self.problem_size)

        self.swap(k, j)
        # print(j, k, [v[:i] for i, v in enumerate(self.tabu_list.tab)])
        # print(self.current_solution)

        current_cost = self.graph.get_path_weight(self.current_solution)
        # print('\t\t',current_cost, self.best_cost)
        if current_cost < self.best_cost and self.tabu_list.tab[j][k] == 0:
            # print(current_cost, self.tabu_list.tab)
            self.best_solution = copy.deepcopy(self.current_solution)
            self.best_cost = current_cost

            self.tabu_list.decrement()
            self.tabu_list.move(j, k, 10)

            self.no_improvement = 0
        else:
            self.no_improvement += 1

    def swap(self, a, b):
        self.current_solution[a], self.current_solution[b] = \
            self.current_solution[b], self.current_solution[a]


class TabuList:
    def __init__(self, dim):
        self.dim = dim
        self.tab = [[0 for _ in range(dim)] for _ in range(dim)]

    def move(self, city1, city2, cadence):
        self.tab[city1][city2] += cadence
        self.tab[city2][city1] += cadence

    def decrement(self):
        tab = self.tab
        for i in range(self.dim):
            for j in range(self.dim):
                tab[i][j] = max(tab[i][j] - 1, 0)

    def __str__(self):
        return '\n'.join(' '.join(map(str, i)) for i in self.tab) + '\n'


if __name__ == '__main__':
    # graph = Graph.from_file('br17.atsp')
    import sys
    graph = Graph.from_file(sys.argv[1])
    print(graph)
    ts = TabuSearch(graph, TabuList(graph.get_dim()))
    print('bef')
    ts.run()
    print('aft')
