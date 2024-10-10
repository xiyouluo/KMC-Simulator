from simulator import Lattice, Species, Simulation, Event
import random

# Define the lattice
size = 20  # 20x20 lattice
lattice = Lattice(size=size)

# Define species
carbon = Species(name='C')

# Define events
def adsorption_event():
    # Choose a random site
    x, y = random.randint(0, size-1), random.randint(0, size-1)
    site = lattice.grid[x][y]
    if site.occupant is None:
        site.occupant = carbon
        print(f"Carbon adsorbed at ({x}, {y})")

def desorption_event():
    # Choose a random occupied site
    occupied_sites = [(x, y) for x in range(size) for y in range(size) if lattice.grid[x][y].occupant == carbon]
    if occupied_sites:
        x, y = random.choice(occupied_sites)
        lattice.grid[x][y].occupant = None
        print(f"Carbon desorbed from ({x}, {y})")

def diffusion_event():
    # Choose a random occupied site
    occupied_sites = [(x, y) for x in range(size) for y in range(size) if lattice.grid[x][y].occupant == carbon]
    if occupied_sites:
        x, y = random.choice(occupied_sites)
        site = lattice.grid[x][y]
        neighbors = lattice.get_neighbors(x, y)
        empty_neighbors = [n for n in neighbors if n.occupant is None]
        if empty_neighbors:
            new_site = random.choice(empty_neighbors)
            new_site.occupant = carbon
            site.occupant = None
            print(f"Carbon diffused from ({x}, {y}) to {new_site.position}")
"""
Implementing Crystallization

To simulate the growth of crystalline carbon, you can modify the diffusion event 
to favor certain directions or implement events for bonding between carbon atoms.

def diffusion_event():
    occupied_sites = [(x, y) for x in range(size) for y in range(size) if lattice.grid[x][y].occupant == carbon]
    if occupied_sites:
        x, y = random.choice(occupied_sites)
        site = lattice.grid[x][y]
        neighbors = lattice.get_neighbors(x, y)
        empty_neighbors = [n for n in neighbors if n.occupant is None]
        if empty_neighbors:
            # Prefer sites next to other carbon atoms to simulate crystallization
            neighbor_scores = []
            for n in empty_neighbors:
                n_neighbors = lattice.get_neighbors(*n.position)
                n_occupied = sum(1 for nn in n_neighbors if nn.occupant == carbon)
                neighbor_scores.append((n, n_occupied))
            # Choose the site with the highest number of occupied neighbors
            max_score = max(score for n, score in neighbor_scores)
            best_sites = [n for n, score in neighbor_scores if score == max_score]
            new_site = random.choice(best_sites)
            new_site.occupant = carbon
            site.occupant = None
            print(f"Carbon diffused from ({x}, {y}) to {new_site.position} (crystallization)")
"""
# Create events
adsorption = Event(
    name='Adsorption',
    rate_constant=1e5,
    activation_energy=0.1,  # eV
    execute_fn=adsorption_event
)

desorption = Event(
    name='Desorption',
    rate_constant=1e5,
    activation_energy=0.2,  # eV
    execute_fn=desorption_event
)

diffusion = Event(
    name='Diffusion',
    rate_constant=1e5,
    activation_energy=0.15,  # eV
    execute_fn=diffusion_event
)

# Initialize simulation
temperature = 800  # K
simulation = Simulation(lattice, [carbon], temperature)

# Add events to the simulation
simulation.add_event(adsorption)
simulation.add_event(desorption)
simulation.add_event(diffusion)

# Run the simulation
total_time = 10.0  # Arbitrary units
simulation.run(total_time)