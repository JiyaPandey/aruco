import cv2 as cv
from cv2 import aruco
import numpy as np

# Load the predefined dictionary
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

# Set parameters for marker detection
param_markers = aruco.DetectorParameters()

# Initialize the camera (default webcam)
cap = cv.VideoCapture(0)

# Check if the camera is accessible
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

print("Press 'q' to quit the video feed.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from the camera.")
        break

    # Convert frame to grayscale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Detect markers
    marker_corners, marker_IDs, _ = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )

    # Draw markers and display IDs if detected
    if marker_corners and marker_IDs is not None:
        aruco.drawDetectedMarkers(frame, marker_corners, marker_IDs)
        for ids, corners in zip(marker_IDs, marker_corners):
            corners = corners.reshape(4, 2).astype(int)
            top_left = corners[0].ravel()
            cv.putText(
                frame,
                f"ID: {ids[0]}",
                (top_left[0], top_left[1] - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
                cv.LINE_AA,
            )
    else:
        cv.putText(
            frame,
            "No ArUco marker detected.",
            (10, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv.LINE_AA,
        )

    # Display the frame
    cv.imshow("ArUco Detection", frame)

    # Exit on pressing 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
