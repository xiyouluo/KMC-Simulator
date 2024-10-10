import math
import random

class Simulation:
    def __init__(self, lattice, species_list, temperature):
        self.lattice = lattice
        self.species_list = species_list
        self.temperature = temperature
        self.time = 0.0
        self.event_queue = []

    def add_event(self, event):
        self.event_queue.append(event)

    def run(self, total_time):
        while self.time < total_time:
            rates = [event.calculate_rate(self.temperature) for event in self.event_queue]
            total_rate = sum(rates)
            if total_rate == 0:
                print("No more events can occur.")
                break

            delta_time = -math.log(random.random()) / total_rate
            self.time += delta_time

            # Select an event
            threshold = random.uniform(0, total_rate)
            cumulative_rate = 0.0
            for event, rate in zip(self.event_queue, rates):
                cumulative_rate += rate
                if cumulative_rate >= threshold:
                    event.execute()
                    break