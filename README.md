# Camera and Lighting Positioning Calculator

"Measure twice. Light once."

This tool is designed to assist photographers, archivists, and digitization specialists in calculating and visualizing the precise geometry required for flat art reproduction and copy work.

Achieving a specific resolution (PPI) while ensuring even lighting coverage involves complex relationships between sensor size, focal length, and physical distances. This Streamlit application automates the math, allowing you to plan your studio setup before moving a single light stand.

## Key Features

* **Precision Positioning:** Calculate the exact distance required between the camera sensor and the artwork to achieve a target PPI.  
* **Lighting Geometry:** Determine optimal light placement (X and Y coordinates relative to the art) to ensure full coverage based on the artwork's dimensions.  
* **Sensor Visualization:** Visual feedback on how much of the camera sensor is utilized by the artwork.  
* **Resolution Limits:** Instantly see the maximum possible PPI for a given lens/camera combination before hitting physical limits.  
* **Diagram Generation:** Auto-generates a downloadable Matplotlib diagram of your specific setup.

## Quick Start

### Streamlit Community Cloud

You can use the live application on Streamlit Community Cloud:

[https://camera-lighting-positioning.streamlit.app/](https://camera-lighting-positioning.streamlit.app/)

### Local Installation

To run the tool on your own machine, follow these steps:

1. **Clone the repository:**  
   ```commandline
   git clone [https://github.com/peterjakubowski/Camera-Lighting-Positioning.git](https://github.com/peterjakubowski/Camera-Lighting-Positioning.git)  
   cd Camera-Lighting-Positioning
   ```

2. **Install dependencies:**  
   It is recommended to use a virtual environment.  
   ```commandline
   pip install -r requirements.txt
   ```

3. **Launch the App:**  
   ```commandline
   streamlit run app.py
   ```

## User Guide

### 1. Configure Equipment

* **Camera Body / Digital Back:** Select your camera from the dropdown menu.  
  * *Note: If your camera is not listed, you can add it manually to data/sensors.json.*  
* **Lens Focal Length:** Choose the focal length of the lens you intend to use (in mm).

### 2. Define the Artwork

* **Dimensions:** Enter the physical width and height of the flat art.  
* **Units:** Toggle between Millimeters (mm), Centimeters (cm), or Inches.

### 3. Set Targets

* **Resolution (PPI):** Input your desired output resolution (e.g., 300 for print, 600 for archive). The app will calculate the distance required to achieve this pixel density.  
* **Light Coverage:** Adjust the radius multiplier.  
  * *1.0*: Lights are positioned to exactly cover the corners of the art (high risk of falloff/vignetting).  
  * *\>1.0*: Moves lights further out to ensure even illumination across the entire surface.

### 4. Interpret the Output

The app provides a data table and a visual diagram. Here is how to read the measurements:

* **Camera Distance:** The distance from the *sensor plane* to the center of the artwork.  
* **Lights Distance X:** How far the lights should be placed to the left/right of the artwork's center (parallel to the wall).  
* **Lights Distance Y:** How far the lights should be placed back from the artwork (perpendicular to the wall).  
* **Sensor Usage:** Percentage of the sensor filled by the artwork. If this is >100%, the art will not fit in the frame, and a warning will appear.  
* **MAX PPI:** The theoretical maximum resolution you can achieve with the current lens/camera combo if you filled the frame completely.

## Tech Stack

* **Streamlit:** UI and interactivity.  
* **Matplotlib:** Dynamic generation of lighting diagrams.  
* **Pydantic:** Data validation for sensor models.  
* **Pandas:** Data presentation.
