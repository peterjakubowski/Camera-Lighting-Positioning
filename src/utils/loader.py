# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/23/2026
# Description:
#

from pathlib import Path
import json

from src.models.sensor import Sensor

SENSORS_JSON_PATH = Path("data/sensors.json")


def load_sensors_from_json(path: Path) -> dict[str, Sensor]:
    """
    Reads a json file and returns a dictionary with camera sensor specs.
    :param path: Path to the json file with sensor specs
    :return: Python dictionary where keys are digital capture names and values are Sensor objects
    """
    _sensors: dict[str, Sensor] = {}
    # load the dictionary of digital camera bodies and backs with sensor size and pixel dimensions
    with open(path, "r") as file:
        sensor_dict = json.loads(file.read())
        for name, attr in sensor_dict.items():
            _sensors[name] = Sensor(**attr)

    return _sensors


sensors = load_sensors_from_json(SENSORS_JSON_PATH)
