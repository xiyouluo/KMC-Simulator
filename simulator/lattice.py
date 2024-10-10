import numpy as np

class Site:
    def __init__(self, position, site_type):
        self.position = position
        self.site_type = site_type
        self.occupant = None  # Occupied by a Species instance or None

class Lattice:
    def __init__(self, size, dimensions=2):
        self.size = size
        self.dimensions = dimensions
        self.grid = np.empty((size, size), dtype=object)
        self._initialize_sites()

    def _initialize_sites(self):
        for x in range(self.size):
            for y in range(self.size):
                position = (x, y)
                self.grid[x][y] = Site(position, site_type='surface')

    def get_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = (x + dx) % self.size, (y + dy) % self.size
            neighbors.append(self.grid[nx][ny])
        return neighbors
