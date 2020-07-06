import csv
import types
from random import randint


def hex_to_rgb(hex_color):
    return tuple(int(hex_color[index: index + 2], 16) for index in range(1, 6, 2))


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            label, hex_color = line
            yield hex_to_rgb(hex_color), label


def generate_colors(count=100):
    return [tuple(randint(0, 255) for _ in range(3)) for __ in range(count)]


def generate_colors_2(count=100):
    for i in range(count):
        yield randint(0, 255), randint(0, 255), randint(0, 255)


def color_distance(color_1, color_2):
    sum_distance_sqr = 0
    for c1, c2 in zip(color_1, color_2):
        sum_distance_sqr += pow((c1 - c2), 2)
    return sum_distance_sqr


def nearest_neighbors(model_colors, target_colors, num_neighbors=5):
    if isinstance(model_colors, types.GeneratorType):
        model_colors = list(model_colors)

    for target in target_colors:
        distances = sorted((color_distance(c[0], target), c) for c in model_colors)
        yield target, distances[:5]


