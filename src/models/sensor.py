# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/23/2026
# Description:
#

from pydantic import BaseModel

# ==============================
# ======== Sensor Info =========
# ==============================


class Sensor(BaseModel):
    sensor_w_mm: float  # width of the sensor in millimeters
    sensor_h_mm: float  # height of the sensor in millimeters
    sensor_w_px: int  # width of the sensor in pixels
    sensor_h_px: int  # height of the sensor in pixels
