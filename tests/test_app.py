# Camera and Lighting Positioning Calculator
#
# Author: Peter Jakubowski
# Date: 9/24/2026
# Description:
#

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from src.utils.loader import sensors

APP_FILE_PATH = Path("app.py")


@pytest.fixture
def at():

    app_test = AppTest.from_file(APP_FILE_PATH)
    app_test.run()
    return app_test


class TestStartUp:

    def test_smoke(self, at: AppTest):

        assert not at.exception, "App should run without any exceptions."

    def test_no_error(self, at: AppTest):

        assert not at.error, "App should start without display an error message."

    def test_app_displays_title_element(self, at: AppTest):

        assert at.title, "App should have a title element"
        assert at.title[0].body == "Camera and Lighting Positioning"

    def test_app_displays_text_markdown(self, at: AppTest):

        assert at.markdown, "App should have a text element"
        assert at.markdown[0].body.startswith("Calculate camera and lighting distances")

    def test_app_displays_figure_image(self, at: AppTest):

        assert len(at.get('imgs')) == 1

    def test_app_display_summary_table(self, at: AppTest):

        assert len(at.table) == 1
        assert at.table[0].value.shape == (13, 2)


class TestSidebarStartup:

    def test_app_displays_sidebar(self, at: AppTest):

        assert at.sidebar, "App should show the side bar"

    def test_app_displays_sidebar_elements(self, at: AppTest):

        assert len(at.sidebar) == 8, "App should display 8 elements in the sidebar"

    def test_app_displays_sidebar_camera_element(self, at: AppTest):

        assert at.sidebar[0].label == "Camera body / digital back"
        assert at.sidebar[0].type == "selectbox"
        assert at.sidebar[0].key == "camera"
        assert len(at.sidebar[0].options) == 13
        assert at.sidebar[0].value.startswith("Canon")

    def test_app_displays_sidebar_lens_focal_length_element(self, at: AppTest):

        assert at.sidebar[1].label == "Lens focal length (mm)"
        assert at.sidebar[1].type == "selectbox"
        assert at.sidebar[1].key == "lens_focal_len_mm"
        assert len(at.sidebar[1].options) == 14
        assert at.sidebar[1].value == 105

    def test_app_displays_sidebar_object_width_element(self, at: AppTest):

        assert at.sidebar[2].label == "Object width"
        assert at.sidebar[2].type == "number_input"
        assert at.sidebar[2].key == "real_object_width"
        assert at.sidebar[2].min == 0.01
        assert at.sidebar[2].max == 100000.0
        assert at.sidebar[2].value == 10.00

    def test_app_displays_sidebar_object_height_element(self, at: AppTest):

        assert at.sidebar[3].label == "Object height"
        assert at.sidebar[3].type == "number_input"
        assert at.sidebar[3].key == "real_object_height"
        assert at.sidebar[3].min == 0.01
        assert at.sidebar[3].max == 100000.0
        assert at.sidebar[3].value == 8.00

    def test_app_displays_sidebar_unit_element(self, at: AppTest):

        assert at.sidebar[4].label == "Unit of measurement"
        assert at.sidebar[4].type == "selectbox"
        assert at.sidebar[4].key == "real_object_units"
        assert len(at.sidebar[4].options) == 3
        assert at.sidebar[4].value == "inches"

    def test_app_displays_sidebar_resolution_element(self, at: AppTest):

        assert at.sidebar[5].label == "Resolution (ppi)"
        assert at.sidebar[5].type == "number_input"
        assert at.sidebar[5].key == "set_ppi"
        assert at.sidebar[5].min == 72
        assert at.sidebar[5].max == 2000
        assert at.sidebar[5].value == 300

    def test_app_displays_sidebar_light_angle_element(self, at: AppTest):

        assert at.sidebar[6].label == "Light angle (degrees)"
        assert at.sidebar[6].type == "slider"
        assert at.sidebar[6].key == "light_angle"
        assert at.sidebar[6].min == 15.0
        assert at.sidebar[6].max == 45.0
        assert at.sidebar[6].value == 38.7

    def test_app_displays_sidebar_light_coverage_element(self, at: AppTest):

        assert at.sidebar[7].label == "Light coverage"
        assert at.sidebar[7].type == "slider"
        assert at.sidebar[7].key == "radius_multiply"
        assert at.sidebar[7].min == 1.0
        assert at.sidebar[7].max == 5.0
        assert at.sidebar[7].value == 2.3


class TestSidebarInput:

    @pytest.mark.parametrize("select_value", sorted(sensors.keys()))
    def test_app_runs_without_exception_when_changing_cameras(self, at: AppTest, select_value: str):

        at.selectbox(key="camera").select(select_value).run()

        assert not at.exception

    @pytest.mark.parametrize("select_value", [24, 45, 50, 55, 85, 90, 100, 105, 110, 120, 135, 150, 200, 240])
    def test_app_runs_without_exception_when_changing_lenses(self, at: AppTest, select_value: int):

        at.selectbox(key="lens_focal_len_mm").select(select_value).run()

        assert not at.exception

    @pytest.mark.parametrize("input_value", [0.01, 100000.0, 10.0, 100.0])
    def test_app_runs_without_exception_when_changing_object_width(self, at: AppTest, input_value: float):

        at.number_input(key="real_object_width").set_value(input_value).run()

        assert not at.exception

    @pytest.mark.parametrize("input_value", [0.01, 100000.0, 8.0, 100.0])
    def test_app_runs_without_exception_when_changing_object_height(self, at: AppTest, input_value: float):

        at.number_input(key="real_object_height").set_value(input_value).run()

        assert not at.exception

    @pytest.mark.parametrize("select_value", ["mm", "cm", "inches"])
    def test_app_runs_without_exception_when_changing_object_units(self, at: AppTest, select_value: str):

        at.selectbox(key="real_object_units").select(select_value).run()

        assert not at.exception

    @pytest.mark.parametrize("input_value", [72, 2000, 100, 300, 600])
    def test_app_runs_without_exception_when_changing_resolution(self, at: AppTest, input_value: int):

        at.number_input(key="set_ppi").set_value(input_value).run()

        assert not at.exception

    @pytest.mark.parametrize("select_value", [15.0, 45.0, 38.7, 30.0])
    def test_app_runs_without_exception_when_changing_light_angle(self, at: AppTest, select_value: float):

        at.slider(key="light_angle").set_value(select_value).run()

        assert not at.exception

    @pytest.mark.parametrize("select_value", [1.0, 5.0, 2.3, 3.0])
    def test_app_runs_without_exception_when_changing_light_coverage(self, at: AppTest, select_value: float):

        at.slider(key="radius_multiply").set_value(select_value).run()

        assert not at.exception


class TestSidebarInputWarnings:

    def test_app_displays_warning_when_ppi_is_too_high(self, at: AppTest):

        at.selectbox(key="camera").select("Canon 5D Mark IV")
        at.number_input(key="real_object_width").set_value(40.0)
        at.number_input(key="real_object_height").set_value(30.0)
        at.selectbox(key="real_object_units").select("cm")
        at.number_input(key="set_ppi").set_value(400)
        at.slider(key="radius_multiply").set_value(1.4)

        at.run()

        assert len(at.warning) == 2
        assert at.warning[0].value.startswith("Warning! The object does not fit in frame at 400ppi.")
        assert at.warning[1].value.startswith("Warning!")

    def test_app_displays_warning_when_light_does_not_cover_entire_viewing_area(self, at: AppTest):

        at.selectbox(key="camera").select("Canon 5D Mark IV")
        at.number_input(key="real_object_width").set_value(40.0)
        at.number_input(key="real_object_height").set_value(30.0)
        at.selectbox(key="real_object_units").select("cm")
        at.number_input(key="set_ppi").set_value(300)
        at.slider(key="radius_multiply").set_value(1.3)

        at.run()

        assert len(at.warning) == 1
        assert at.warning[0].value.startswith("Warning! The light coverage does not cover the entire viewing area.")
