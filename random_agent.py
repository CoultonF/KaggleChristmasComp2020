import random

def agent(observation, configuration):
    bandit = random.randint(0, configuration['banditCount'] - 1)
    return bandit
