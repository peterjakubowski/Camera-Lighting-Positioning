# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 2/14/2025
# Description:
#

from pydantic import BaseModel


class Sensor(BaseModel):
    sensor_w_mm: float
    sensor_h_mm: float
    sensor_w_px: int
    sensor_h_px: int
