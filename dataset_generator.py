import csv
from random import randint


def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i: i + 2], 16) for i in range(1, 6, 2))


def load_colors(filename):
    with open('colors.csv') as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            label, hex_color = line
            yield hex_to_rgb(hex_color), label


def generate_colors(count=100):
    return [tuple(randint(0, 255) for c in range(3)) for r in range(count)]


def generate_colors_2(count=100):
    for i in range(count):
        yield randint(0, 255), randint(0, 255), randint(0, 255)
