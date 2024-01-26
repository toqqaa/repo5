import cv2

# Replace these values with your own
image_path = r"D:\Lecturs\Machine Vision\Machine_vision_code\Pics\people1.jpg"
class_index = 0  # Index of the object class
box_coords = [100, 200, 500, 600]  # Coordinates of the bounding box in pixel values

# Read the image to get its dimensions
image = cv2.imread(image_path)
height, width, _ = image.shape

# Normalize the coordinates
center_x = (box_coords[0] + box_coords[2])import cv2

# Replace these values with your own
image_path = r"D:\Lecturs\Machine Vision\Machine_vision_code\Pics\people1.jpg"
class_index = 0  # Index of the object class
box_coords = [100, 200, 500, 600]  # Coordinates of the bounding box in pixel values

# Read the image to get its dimensions
image = cv2.imread(image_path)
height, width, _ = image.shape

# Normalize the coordinates
center_x = (box_coords[0] + box_coords[2]) / (2.0 * width)
center_y = (box_coords[1] + box_coords[3]) / (2.0 * height)
box_width = (box_coords[2] - box_coords[0]) / width
box_height = (box_coords[3] - box_coords[1]) / height

# Write to the YOLO annotation file
annotation_file_path = "D:\Lecturs\Machine Vision\Machine_vision_code\image.txt"
with open(annotation_file_path, "w") as f:
    f.write(f"{class_index} {center_x} {center_y} {box_width} {box_height}")
