# Motion Detection and Alarm System (OOP Version)

This project is an object-oriented Python implementation of a motion detection and alarm system using OpenCV. The system uses the webcam to monitor motion and triggers an audible alarm when motion is consistently detected.

## Features

- Live webcam feed using OpenCV.
- Frame preprocessing (grayscale, Gaussian blur) for motion detection.
- Threshold-based motion detection using frame difference.
- Toggleable alarm system with beeping sound.
- Organized with Object-Oriented Programming (OOP) principles.

## File Structure

- `camera_base.py`: Handles camera initialization and frame reading.
- `frame_processor.py`: Preprocesses frames (resize, grayscale, blur).
- `motion_detector.py`: Controls the motion detection logic.
- `alarm_manager.py`: Manages the alarm state and beeping in a separate thread.
- `main.py`: Runs the motion detection application.

## Controls

- Press `t` to toggle the alarm mode on/off.
- Press `q` to quit the application.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- imutils (`imutils`)
- Windows OS (for `winsound` module)

Install dependencies with:

```bash
pip install opencv-python imutils

## Credits

This project is a refactored version of the motion detection tutorial by [NeuralNine](https://www.youtube.com/@NeuralNine).  
Original video: [Motion Detection with Python and OpenCV](https://youtu.be/QPjPyUJeYYE?si=euYzIMx3-ZLW6EZl)

Converted to an Object-Oriented Programming (OOP) structure for better modularity and readability.
