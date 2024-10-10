import math
import random

k_b = 8.617333262145e-5  # Boltzmann constant in eV/K

class Event:
    def __init__(self, name, rate_constant, activation_energy, execute_fn):
        self.name = name
        self.rate_constant = rate_constant
        self.activation_energy = activation_energy
        self.execute_fn = execute_fn  # Function to execute the event

    def calculate_rate(self, temperature):
        return self.rate_constant * math.exp(-self.activation_energy / (k_b * temperature))

    def execute(self):
        self.execute_fn()