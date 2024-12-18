# **Lane Detection using OpenCV**

**202234892 Sihu Park**

Python-based lane detection system using OpenCV. This project processes video footage to detect lane markings on the road, highlight the lane area, and visualize the results in real time. The system is ideal for beginners exploring computer vision and provides a solid foundation for advanced applications such as self-driving car projects.


## **Features**
- Detects lane markings in video footage using edge detection and Hough Transform.
- Highlights the detected lane marking.
- Real-time processing with adjustable region of interest (ROI).

## **Requirements**
### **1. Dependencies**
This project requires Python 3.7 or later and the following libraries:
- OpenCV: `opencv-python`
- NumPy: `numpy`

Install dependencies using pip:
```bash
pip install opencv-python numpy
```

### **2. Video Input**
Provide any video with visible lane markings. You can use the sample video I took. The default path for the video is `Footage/tunnel.mp4`. Update this path in main.py if necessary!


## **How It Works**
### **Pipeline Overview**
1. **Frame Preprocessing**
    - Convert frames to grayscale.
    - Apply Gaussian blur to reduce noise.
    - Perform Canny edge detection to highlight lane markings.
2. **Region of Interest**
    - Mask irrelevant parts of the frame, focusing only on the road area.
3. **Lane Detection**
    - Use Hough Transform to detect lane lines.
4. **Lane Visualization**
    - Draw lane lines on the video.


## **Usage**

### **1. Add your Footage**
Place your video file in the Footage/ directory. Update the path in `main.py` if using a different filename.
### **2. Run the Program**
Execute the script:
```bash
python main.py
```
### **3. Controls**
Press `q`: Exit the video playback.


## **Sample Results**
![demo](https://github.com/user-attachments/assets/d09dad01-8c37-41a6-9dbf-4bbe4f6c9416)


## **Customization**
### **Adjust Region Of Interest**
Modify the `region_of_interest()` function in `utils.py` to change the focus area. Adjust the polygon points to fit your specific video or lane layout.
```Python
polygon = np.array([[
(int(width * 0.2), height),              # DL
(int(width * 0.8), height),             # DR
(int(width * 0.55), int(height * 0.75)),  # UR
(int(width * 0.45), int(height * 0.75))   # UL
]], np.int32)
```


## **Future Improvements**
- Implement distortion correction using camera calibration.
- Support real-time video from a webcam or live feed.


## **References**
- OpenCV Documentation: [Link](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- LearnOpenCV - How to Find Frame Rate or Frames Per Second (FPS) in OpenCV: [Link](https://learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/)
