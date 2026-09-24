# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 2/14/2025
# Description: Calculate camera and lighting distances for flat art and copywork setups.
#

from io import BytesIO

import pandas as pd
import streamlit as st

from src.utils import math
from src.utils.loader import sensors
from src.utils.tools import (
    calculate_max_ppi,
    convert_units,
    print_measurements,
)
from src.utils.viz import plot_lighting_diagram

# ==============================
# ========= Streamlit ==========
# ==============================

st.set_page_config(
    page_title="Camera and Lighting Positioning",
    layout="centered"
)

st.title('Camera and Lighting Positioning')

st.write('Calculate camera and lighting distances for flat art and copywork setups.')

st.divider()

# ==============================
# ======== Form fields =========
# ==============================

with (st.sidebar):
    # select the camera or digital back name
    st.selectbox(label="Camera body / digital back",
                 key="camera",
                 options=sorted(sensors.keys())
                 )

    # select the lens focal length
    st.selectbox(label="Lens focal length (mm)",
                 key="lens_focal_len_mm",
                 options=[24, 45, 50, 55, 85, 90, 100, 105, 110, 120, 135, 150, 200, 240],
                 index=7
                 )

    # set the object width, physical measurement
    st.number_input(label="Object width",
                    key="real_object_width",
                    min_value=0.0,
                    max_value=100000.0,
                    step=0.01,
                    value=10.00
                    )

    # set the object height, physical measurement
    st.number_input(label="Object height",
                    key="real_object_height",
                    min_value=0.0,
                    max_value=100000.0,
                    step=0.01,
                    value=8.00
                    )

    # select the unit of measurement used to measure the width and height of the artwork
    st.selectbox(label="Unit of measurement",
                 key="real_object_units",
                 options=["mm", "cm", "inches"],
                 index=2,
                 )

    # set the desired resolution in pixels per inch (ppi)
    st.number_input(label="Resolution (ppi)",
                    key="set_ppi",
                    min_value=72,
                    max_value=2000,
                    step=1,
                    value=300
                    )

    # set the lighting angle, defaults to standard (~38)
    st.slider(label="Light angle (degrees)",
              key="light_angle",
              min_value=15.0,
              max_value=45.0,
              step=0.1,
              value=38.7
              )

    # set to desired radius multiplier to control light coverage.
    st.slider(label="Light coverage",
              key="radius_multiply",
              min_value=1.0,
              max_value=5.0,
              step=0.05,
              value=2.3
              )

# sensor object for the selected camera/sensor
sensor = sensors[st.session_state.camera]

# ==============================
# ========= Calculate ==========
# ==============================

# convert real object width and height to inches if provided in cm or mm
if st.session_state.real_object_units == 'cm':
    real_object_width = math.convert_cm_to_inches(st.session_state.real_object_width)
    real_object_height = math.convert_cm_to_inches(st.session_state.real_object_height)

elif st.session_state.real_object_units == 'mm':
    real_object_width = math.convert_mm_to_inches(st.session_state.real_object_width)
    real_object_height = math.convert_mm_to_inches(st.session_state.real_object_height)

else:
    real_object_width = st.session_state.real_object_width
    real_object_height = st.session_state.real_object_height

# check max ppi
if st.session_state.set_ppi > (max_ppi := calculate_max_ppi(sensor, real_object_width, real_object_height)):
    st.warning(f"Warning! The object does not fit in frame at {st.session_state.set_ppi}ppi. "
               f"The maximum possible ppi is {max_ppi}")

# calculate object width and height in pixels by multiplying ppi by object measurements in inches
object_w_px = math.calculate_object_pixels(st.session_state.set_ppi, real_object_width)
object_h_px = math.calculate_object_pixels(st.session_state.set_ppi, real_object_height)

# calculate object width and height in mm on sensor by multiplying sensor size in mm by object
# size in pixels and dividing by the sensor size in pixels
object_w_on_film_mm = math.calculate_object_mm_size_on_sensor(object_w_px, sensor.sensor_w_mm, sensor.sensor_w_px)
object_h_on_film_mm = math.calculate_object_mm_size_on_sensor(object_h_px, sensor.sensor_h_mm, sensor.sensor_h_px)

# calculate object resolution by dividing object in pixels by object in inches (should equal set_ppi value)
pixels_per_inch = math.calculate_resolution_pixels_per_inch(object_w_px, real_object_width)

# calculate distance from camera to object
# multiply object width by lens focal length and divide by object size on sensor
camera_distance = math.calculate_camera_distance_to_object_inches(
    real_object_width, object_w_on_film_mm, st.session_state.lens_focal_len_mm)

# calculate how much of the sensor is used
sensor_usage_w = math.calculate_sensor_usage_percent(object_w_on_film_mm, sensor.sensor_w_mm)
sensor_usage_h = math.calculate_sensor_usage_percent(object_h_on_film_mm, sensor.sensor_h_mm)
# calculate the width and height dimensions of what is in view
max_w_in = sensor.sensor_w_px / pixels_per_inch
max_h_in = sensor.sensor_h_px / pixels_per_inch

# Radius calculation
object_radius = math.calculate_radius_of_rectangle_inside_circle(real_object_width, real_object_height)
# radius = math.calculate_radius(real_object_width, st.session_state.radius_multiply)
# calculate the radius of the object in a circle, multiplied by the radius multiplier
light_radius = math.calculate_radius_of_rectangle_inside_circle(
    real_object_width * st.session_state.radius_multiply,
    real_object_height * st.session_state.radius_multiply
)
# Convert degrees to radians for Python's math functions
angle_radians = math.convert_angle_degrees_to_radians(st.session_state.light_angle)

y_multiplier = math.calculate_y_multiplier(angle_radians)

# calculate the position of lights on x and y-axis, distance from the center of the object
light_distance_x_axis = math.calculate_light_position_x_axis(light_radius)
light_distance_y_axis = math.calculate_light_position_y_axis(light_radius, y_multiplier)

# =======================
# ====== Warnings =======
# =======================

# calculate the radius of the rectangle in view, what the sensor sees, the image area
radius_in_view = math.calculate_radius_of_rectangle_inside_circle(max_w_in, max_h_in)

# check light coverage, does the light cover everything in the camera's view?
if light_radius < radius_in_view:
    # what do I have to multiply the object's radius by to get the in view radius?
    min_required_multiplier = math.round_up_to_nearest_05(radius_in_view / object_radius)

    st.warning("Warning! The light coverage does not cover the entire viewing area. "
               f"Increase light coverage to a minimum of {round(min_required_multiplier, 2)}")

# check that the object fits in the frame
if object_w_on_film_mm > sensor.sensor_w_mm:
    st.warning("Warning! The object width does not fit in frame.")
if object_h_on_film_mm > sensor.sensor_h_mm:
    st.warning("Warning! The object height does not fit in frame.")

# ============================
# ====== Plot diagrams =======
# ============================

lighting_diagram = plot_lighting_diagram(
    real_object_width=real_object_width,
    real_object_height=real_object_height,
    radius=light_radius,
    distance=camera_distance,
    light_1x=light_distance_x_axis,
    light_1y=light_distance_y_axis,
    max_w_in=max_w_in,
    max_h_in=max_h_in)

# Create a buffer for the figure
buf = BytesIO()
# Save the figure in the buffer
lighting_diagram.savefig(buf, format='png')
# Display the figure buffer image
st.image(buf)

# ======================
# ====== Summary =======
# ======================

summary = [("Camera", st.session_state.camera),
           ("Lens focal length", f"{st.session_state.lens_focal_len_mm}mm"),
           ("Sensor size mm", f"{sensor.sensor_w_mm} x {sensor.sensor_h_mm}"),
           ("Sensor size pixels", f"{sensor.sensor_w_px} x {sensor.sensor_h_px}"),
           ("Sensor usage width", f"{sensor_usage_w}%"),
           ("Sensor usage height", f"{sensor_usage_h}%"),
           ("Camera to object distance", f"{print_measurements(convert_units(camera_distance, "inches"))}"),
           ("Lights distance x", f"{print_measurements(convert_units(light_distance_x_axis, "inches"))}"),
           ("Lights distance y", f"{print_measurements(convert_units(light_distance_y_axis, "inches"))}"),
           ("Object width", f"{print_measurements(convert_units(real_object_width, "inches"))}"),
           ("Object height", f"{print_measurements(convert_units(real_object_height, "inches"))}"),
           ("Object dimensions pixels", f"{object_w_px} x {object_h_px}"),
           ("Object resolution (ppi)", f"{pixels_per_inch}")
           ]

df = pd.DataFrame(data=summary, columns=[0, 1])

st.table(df)
