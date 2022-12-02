'''
Project Name: Random Walk
Author: Ryan Coutts
Due Date: 2022-11-18
Course: CS1400-X01

This program takes 3 parameters form the command line (list of walk lengths,
number of trials for each walk length, and character to be simulated). It then
will print out certain stats from each character and simulation that it ran.
Finally, the program plots out the end points of a random walk of 100 steps,
ran 50 times, for each character.
'''

import subprocess
import tempfile
import sys
import math
from statistics import mean
import statistics
import random
import turtle

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs',
                        '-dSAFER',
                        '-o',
                        dest,
                        '-r200',
                        '-dEPSCrop',
                        '-sDEVICE=png16m',
                        tmp.name],
                       stdout=subprocess.DEVNULL)

def simulate(walk_lengths, trials, character):
    '''Runs the randon walk simulations for the given character(s)'''
    if character.lower() == "pa":
        pa_(walk_lengths, trials)
    elif character.lower() == "mi-ma":
        mima(walk_lengths, trials)
    elif character.lower() == "reg":
        reg(walk_lengths, trials)
    elif character.lower() == "all":
        all_char(walk_lengths, trials)
    else:
        print(f'"{character}" is not a character. please use "Pa", '
            '"Mi-Ma", "Reg", or "All" (not case-sensitive).')

def pa_(walk_lengths, trials):
    '''Runs Pa's random walk simulation'''
    odds = ["north", "east", "south", "west"]
    for length in walk_lengths:
        print_stats(length, trials, "Pa", odds)

def mima(walk_lengths, trials):
    '''Runs Mi-Ma's random walk simulation'''
    odds = ["north", "east", "south", "south", "west"]
    for length in walk_lengths:
        print_stats(length, trials, "Mi-Ma", odds)

def reg(walk_lengths, trials):
    '''Runs Reg's random walk simulation'''
    odds = ["east", "west"]
    for length in walk_lengths:
        print_stats(length, trials, "Reg", odds)

def all_char(walk_lengths, trials):
    '''Runs all 3 characters' random walk simulations'''
    pa_(walk_lengths, trials)
    mima(walk_lengths, trials)
    reg(walk_lengths, trials)

def print_stats(length, trials, character, odds):
    '''Prints the Mean, CV, Max distance, and Min distance of a walk'''
    data = find_distances(length, trials, odds)
    average = round(mean(data), 1)
    cv_ = round(statistics.stdev(data) / average, 1)
    print(f"{character} random walk of {length} steps")
    print(f"Mean = {average} CV = {cv_}")
    print(f"Max = {round(max(data), 1)} Min = {round(min(data), 1)}")

def find_distances(length, trials, odds):
    '''Creates a list of end points and returns their distance from center'''
    end_points = []
    distances = []
    for _ in range(int(trials)):
        end_points.append(find_end_point(length, odds))
    for tup in end_points:
        distance = distance_from_axis(tup[0], tup[1])
        distances.append(distance)
    return distances

def find_end_point(walk_length, odds):
    '''Returns the end point of a single walk'''
    x_axis = 0
    y_axis = 0
    for _ in range(int(walk_length)):
        direction = random.choice(odds)
        if direction == "north":
            y_axis += 1
        elif direction == "east":
            x_axis += 1
        elif direction == "south":
            y_axis -= 1
        elif direction == "west":
            x_axis -= 1
    return (x_axis, y_axis)

def distance_from_axis(x_value, y_value):
    '''Finds the distance from the center to a given coordinate'''
    return(math.sqrt((x_value ** 2) + (y_value ** 2)))

def scale_cord5(tup):
    '''Scales both coordinates by 5 times'''
    return (tup[0] * 5, tup[1] *5)

def plot():
    '''Plots the end points of all characters' walks'''
    pa_walk = ["north", "east", "south", "west"]
    mima_walk = ["north", "east", "south", "south", "west"]
    reg_walk = ["east", "west"]
    turtle.screensize(canvwidth = 300, canvheight = 400)
    turtle.shapesize(0.5, 0.5)
    turtle.speed(10)
    turtle.up()
    for _ in range(50):
        pa_point = scale_cord5(find_end_point(100, pa_walk))
        turtle.shape('circle')
        turtle.color('black')
        turtle.goto(pa_point[0], pa_point[1])
        turtle.stamp()
    for _ in range(50):
        turtle.shape("square")
        turtle.color("green")
        mima_point = scale_cord5(find_end_point(100, mima_walk))
        turtle.goto(mima_point[0], mima_point[1])
        turtle.stamp()
    for _ in range(50):
        turtle.shape("triangle")
        turtle.color("red")
        reg_point = scale_cord5(find_end_point(100, reg_walk))
        turtle.goto(reg_point[0], reg_point[1])
        turtle.stamp()
    save_to_image()

def main():
    '''Main function of the program'''
    simulate(sys.argv[1].split(","), int(sys.argv[2]), sys.argv[3])
    plot()
    turtle.mainloop()

if __name__ == "__main__":
    main()














