import cv2
import numpy as np

def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, 50, 150)

    return edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    polygon = np.array([[
    (int(width * 0.2), height),              # DL
    (int(width * 0.8), height),             # DR
    (int(width * 0.55), int(height * 0.7)),  # UR
    (int(width * 0.45), int(height * 0.7))   # UL
]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    return masked_edges


def detect_lanes(masked_edges, frame):
    lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi/180, threshold=70, 
                            minLineLength=40, maxLineGap=600)
    
    line_image = np.zeros_like(frame)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)

    combined = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    return combined