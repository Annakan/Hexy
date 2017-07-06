import numpy as np
import pygame as pg

import hexy as hx


def make_hex_surface(color, radius, border_color=(100, 100, 100), border=True, hollow=False):
    """
    Draws a hexagon with gray borders on a pygame surface.
    :param color: The fill color of the hexagon.
    :param radius: The radius (from center to any corner) of the hexagon.
    :param border_color: Color of the border.
    :param border: Draws border if True.
    :param hollow: Does not fill hex with color if True.
    :return: A pygame surface with a hexagon drawn on it
    """
    points = []
    for i in range(6):
        angle = np.deg2rad(30 * (2 * i + 1))
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append((x, y))

    points = np.array(points)

    sorted_x = sorted(points[:, 0])
    sorted_y = sorted(points[:, 1])
    minx = sorted_x[0]
    maxx = sorted_x[-1]
    miny = sorted_y[0]
    maxy = sorted_y[-1]

    center = ((maxx - minx + 10) / 2, (maxy - miny + 10) / 2)
    surface = pg.Surface(map(int, (maxx - minx + 10, maxy - miny + 10)))
    surface.set_colorkey((0, 0, 0))
    if len(color) >= 4:
        surface.set_alpha(color[-1])
    if not hollow:
        pg.draw.polygon(surface, color, points + center, 0)

    if border or (not hollow):
        pg.draw.polygon(surface, border_color, points + center, 4)
    return surface


class MyHex(hx.HexTile):
    def __init__(self, axial_coordinates=(0, 0, 0), color=(128, 0, 0), radius=20):
        self.axial_coordinates = axial_coordinates
        self.position = hx.hex_to_pixel(hx.axial_to_cube(axial_coordinates), radius)
        self.color = color
        self.radius = radius
        self.image = make_hex_surface(color, radius)
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_draw_position(self):
        """
        Get the location to draw this hex so that the center of the hex is at `self.position`.
        :return: The location to draw this hex so that the center of the hex is at `self.position`.
        """
        return self.position - [self.image.get_width() / 2, self.image.get_height() / 2]
