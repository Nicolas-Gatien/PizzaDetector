import sys
import neat
import time
import os, random
from PIL import Image

# Define the fitness function for the NEAT algorithm
def eval_genomes(genomes, config):
    nets = []
    ge = []
    
    for genome_id, genome in genomes:
        # Set up the neural network for the genome
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
        ge.append(genome)

    # Run the game simulation
    for j in range(0, 20):
        # Get the input for the neural network
        img_name = random.choice(os.listdir("D:\Image Recognizer\processed data")) #change dir name to whatever
        img = Image.open(f'D:/Image Recognizer/processed data/{img_name}').convert('RGB')
        width, height = img.size
        pixel_values = list(img.getdata())
        inputs = []
        for x in range(width):
            for y in range(height):
                pixels = pixel_values[width*y+x]
                if type(pixels) is not int:
                    for item in pixels:
                        inputs.append(item)
    
        goal = 2
        if "pizza" in img_name:
            goal = 1
        else: 
            goal = 0

        for x, net in enumerate(nets):
            # Use the neural network to determine the player's movement
            actions = net.activate(inputs)
            if actions[0] > actions[1]: # Not Pizza:
                if goal == 0: # Goal = not pizza
                    ge[x].fitness += 1

            if actions[1] > actions[0]: # Is Pizza:
                if goal == 1: # Goal = pizza
                    ge[x].fitness += 1

# Set up the NEAT configuration
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    'config-feedforward.txt')

# Create the population
population = neat.Population(config)

# Add a reporter to show progress in the terminal
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)


# Run the NEAT algorithm
winner = population.run(eval_genomes, 250)
stats.save()
