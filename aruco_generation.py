import cv2 as cv
from cv2 import aruco
import os

# Dictionary to specify the type of the marker
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

# Marker size and ID range
MARKER_SIZE = 400  # pixels
NUM_MARKERS = 1  # generating 20 markers

# Create the "markers" folder if it doesn't exist
if not os.path.exists("markers"):
    os.makedirs("markers")

# Generating unique markers using a loop
for marker_id in range(NUM_MARKERS):
    # Generate the marker
    marker_image = aruco.generateImageMarker(marker_dict, marker_id, MARKER_SIZE)

    # Show the marker
    cv.imshow(f"Marker {marker_id}", marker_image)
    
    # Save the marker image
    cv.imwrite(f"markers/marker_{marker_id}.png", marker_image)

    # Wait for a key press to continue to the next marker (you can also remove this to skip waiting)
    key = cv.waitKey(0)
    if key == 27:  # If 'ESC' is pressed, break the loop
        break

# Close all OpenCV windows
cv.destroyAllWindows()

print(f"Generated {NUM_MARKERS} markers and saved them in the 'markers' folder.")
