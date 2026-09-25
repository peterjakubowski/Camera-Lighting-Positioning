# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/23/2026
# Description:
#

import math

# ==========================
# ====== Conversions =======
# ==========================


def convert_cm_to_inches(value: float) -> float:

    return value * 0.393701


def convert_mm_to_inches(value: float) -> float:

    return value * 0.0393701


def convert_inches_to_cm(value: float) -> float:

    return value / .393701


def convert_inches_to_mm(value: float) -> float:

    return value / 0.0393701


def convert_angle_degrees_to_radians(angle_degrees: float) -> float:

    return math.radians(angle_degrees)

# ==============================
# ========= Calculate ==========
# ==============================


def calculate_sensor_ratio(sensor_w_px: int, sensor_h_px: int) -> float:

    return sensor_w_px / sensor_h_px


def calculate_object_pixels(ppi: int, object_inches: float) -> int:

    return int(ppi * object_inches)


def calculate_object_mm_size_on_sensor(object_px: int, sensor_mm: float, sensor_px: float) -> float:

    return (sensor_mm * object_px) / sensor_px


def calculate_resolution_pixels_per_inch(object_pixels: int, object_inches: float) -> float:

    return object_pixels / object_inches


def calculate_camera_distance_to_object_inches(object_inches: float, object_mm_on_sensor: float, lens_focal_len_mm: int) -> float:

    return (object_inches * lens_focal_len_mm) / object_mm_on_sensor


def calculate_radius(object_width_inches: float, multiplier: float) -> float:

    return (object_width_inches * multiplier) / 2


def calculate_y_multiplier(angle_radians: float) -> float:

    return 2.5 * math.tan(angle_radians)


def calculate_light_position_x_axis(radius: float) -> float:

    return radius * 2.5


def calculate_light_position_y_axis(radius: float, multiplier: float) -> float:

    return radius * multiplier


def calculate_sensor_usage_percent(object_mm: float, sensor_mm: float) -> float:

    return round((object_mm / sensor_mm) * 100, 2)


def calculate_radius_of_rectangle_inside_circle(width: float, height: float) -> float:
    """
    Calculate the radius of a circumscribed rectangle (a rectangle inside a circle).
    The radius is the distance from the rectangle's center to any of it's four corners.
    :param width: Width of the rectangle
    :param height: Height of the rectangle
    :return:
    """
    a = width / 2
    b = height / 2
    # calculate the hypotenuse of a triangle
    c = (a ** 2 + b ** 2) ** 0.5

    return c


def round_up_to_nearest_05(n: float) -> float:

    return math.ceil(n * 20) / 20
