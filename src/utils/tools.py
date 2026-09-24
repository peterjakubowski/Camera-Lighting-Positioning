# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 2/14/2025
# Description:
#


from fractions import Fraction
from typing import Literal

from numpy import floor

from src.models.sensor import Sensor
from src.utils import math


def calculate_max_ppi(sensor: Sensor, real_object_width: float, real_object_height: float):
    """

    :param sensor: Sensor object
    :param real_object_width: Width of the real object in inches
    :param real_object_height: Height of the real object in inches
    :return:
    """

    sensor_ratio = math.calculate_sensor_ratio(sensor.sensor_w_px, sensor.sensor_h_px)
    max_w_px = int(floor(sensor.sensor_w_px / real_object_width))
    max_h_px = int(floor(sensor.sensor_h_px / real_object_height))

    if real_object_width >= real_object_height * sensor_ratio:
        return max_w_px

    return max_h_px


def convert_units(measurement: float, unit: Literal["mm", "cm", "inches"] = "inches") -> tuple[float, float, float]:
    """
    Convert a measurement to all three units: cm, mm, and inches

    :param measurement: the measurement to convert
    :param unit: string unit of measurement, mm, cm, or in
    :return: tuple of measurement in mm, cm, and in
    """

    if unit == 'cm':
        measurement = math.convert_cm_to_inches(measurement)
    elif unit == 'mm':
        measurement = math.convert_mm_to_inches(measurement)

    return math.convert_inches_to_mm(measurement), math.convert_inches_to_cm(measurement), measurement


def print_measurements(measurements: tuple[float, float, float]) -> str:
    """
    Utility to format a string of measurements for printing

    Example output: "4088.9 mm / 408.89 cm / 160.98 in / 13 ft 4 49/50 in"

    :param measurements: tuple of measurements mm, cm, in
    :return: string
    """

    mm, cm, inches = measurements
    string = ""
    string += str(round(mm, 2)) + " mm | "
    string += str(round(cm, 2)) + " cm | "
    string += str(round(inches, 2)) + " in | "
    if inches // 12 > 0:
        string += str(int(inches // 12)) + " ft"
    if floor(inches % 12) > 0:
        string += " " + str(int(floor(inches % 12)))
    if round(inches - int(inches), 1) > 0:
        string += " " + str(Fraction(str(round(inches - int(inches), 2))))
    string += " in"

    return string
