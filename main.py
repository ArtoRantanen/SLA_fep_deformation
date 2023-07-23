import matplotlib.pyplot as plt
import numpy as np
import time


def set_size(len):
    nm_len = round(len * 1000000 / 405)
    return nm_len


def create_matrix(x, y):
    matrix = []
    for i in range(x):
        matrix.append([[0, 90]] * y)
    return matrix


# wave
class Physics:
    wave_len = 405 / 1000000  # in nanometres


# printer characteristics
class Printer:
    len_x = 1
    len_y = 2
    build_plate_height = 0.05
    fep_thickness = 0.125


# damage characteristics
class Damage:
    damage_center = [5, 5]
    damage_radius = 0.6
    damage_depth = 0.06


pixel_x, pixel_y = set_size(Printer.len_x), set_size(Printer.len_y)

damage_center_nm = []
for i in Damage.damage_center:
    damage_center_nm.append(set_size(i))
damage_radius_nm = set_size(Damage.damage_radius)
damage_depth_nm = set_size(Damage.damage_depth)

create_matrix(pixel_x, pixel_y)
