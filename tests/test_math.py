# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/24/2026
# Description:
#

from src.utils import math


class TestConvertTypes:

    def test_math_convert_cm_to_inches_returns_float(self):

        result = math.convert_cm_to_inches(value=10.0)

        assert isinstance(result, float)

    def test_math_convert_mm_to_inches_returns_float(self):

        result = math.convert_mm_to_inches(value=10.0)

        assert isinstance(result, float)

    def test_math_convert_inches_to_cm_returns_float(self):

        result = math.convert_inches_to_cm(value=10.0)

        assert isinstance(result, float)

    def test_math_convert_inches_to_mm_returns_float(self):

        result = math.convert_inches_to_mm(value=10.0)

        assert isinstance(result, float)

    def test_math_convert_angle_degrees_to_radians_returns_float(self):

        result = math.convert_angle_degrees_to_radians(10.0)

        assert isinstance(result, float)


class TestCalculateTypes:

    def test_calculate_sensor_ratio_returns_float(self):

        result = math.calculate_sensor_ratio(sensor_w_px=100,sensor_h_px=100)

        assert isinstance(result, float)

    def test_calculate_object_pixels_returns_int(self):

        result = math.calculate_object_pixels(ppi=300, object_inches=10.0)

        assert isinstance(result, int)

    def test_calculate_object_mm_size_on_sensor_returns_float(self):

        result = math.calculate_object_mm_size_on_sensor(object_px=100, sensor_mm=10.0, sensor_px=10)

        assert isinstance(result, float)

    def test_calculate_resolution_pixels_per_inch_returns_float(self):

        result = math.calculate_resolution_pixels_per_inch(object_pixels=100, object_inches=10.0)

        assert isinstance(result, float)

    def test_calculate_camera_distance_to_object_inches_returns_float(self):

        result = math.calculate_camera_distance_to_object_inches(object_inches=10.0, object_mm_on_sensor=10.0, lens_focal_len_mm=105)

        assert isinstance(result, float)

    def test_calculate_radius_returns_float(self):

        result = math.calculate_radius(object_width_inches=10.0, multiplier=1.0)

        assert isinstance(result, float)

    def test_calculate_y_multiplier_returns_float(self):

        result = math.calculate_y_multiplier(angle_radians=10.0)

        assert isinstance(result, float)

    def test_calculate_light_position_x_axis_returns_float(self):

        result = math.calculate_light_position_x_axis(radius=10.0)

        assert isinstance(result, float)

    def test_calculate_light_position_y_axis_returns_float(self):

        result = math.calculate_light_position_y_axis(radius=10.0, multiplier=1.0)

        assert isinstance(result, float)

    def test_calculate_sensor_usage_percent_returns_float(self):

        result = math.calculate_sensor_usage_percent(object_mm=10.0, sensor_mm=10.0)

        assert isinstance(result, float)

    def test_calculate_radius_of_rectangle_inside_circle_returns_float(self):

        result = math.calculate_radius_of_rectangle_inside_circle(width=10.0, height=10.0)

        assert isinstance(result, float)

    def test_round_up_to_nearest_05_returns_float(self):

        result = math.round_up_to_nearest_05(10.0)

        assert isinstance(result, float)
