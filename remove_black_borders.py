import cv2
import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

print_lock = Lock()

class BorderAnalyzer:
    def __init__(self, white_threshold=85):
        self.white_threshold = white_threshold

    def find_borders(self, img_path):
        img = cv2.imread(img_path)
        if img is None:
            print("Image not found.")
            return None, None, None, None

        # Convert to Grayscale to simplify image processing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        left_border = 0
        right_border = w - 1
        top_border = 0
        bottom_border = h - 1

        # Find left border
        for i in range(w):
            col = gray[:, i]
            if np.mean(col) > self.white_threshold:
                left_border = i
                break

        # Find right border
        for i in range(w - 1, -1, -1):
            col = gray[:, i]
            if np.mean(col) > self.white_threshold:
                right_border = i
                break

        # Find top border
        for i in range(h):
            row = gray[i, :]
            if np.mean(row) > self.white_threshold:
                top_border = i
                break

        # Find bottom border
        for i in range(h - 1, -1, -1):
            row = gray[i, :]
            if np.mean(row) > self.white_threshold:
                bottom_border = i
                break

        return left_border, right_border, top_border, bottom_border

class ImageCropper:
    def crop_image(self, img_path, left_border, right_border, top_border, bottom_border, output_folder, target_width=None, target_height=None):
        img = cv2.imread(img_path)
        if img is None:
            with print_lock:
                print("Image not found.")
            return

        cropped_img = img[top_border:bottom_border, left_border:right_border]

        if target_width and target_height:
            cropped_img = cv2.resize(cropped_img, (target_width, target_height))

        output_path = os.path.join(output_folder, os.path.basename(img_path))
        cv2.imwrite(output_path, cropped_img)

        with print_lock:
            if target_width and target_height:
                print(f"Saved cropped and resized image to {output_path}")
            else:
                print(f"Saved cropped image to {output_path}")

def ensure_output_folder_exists(output_folder, input_folder):
    if output_folder is None:
        output_folder = "cropped_" + input_folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder

def process_image(filename, input_folder, output_folder, target_width, target_height):
    output_folder = ensure_output_folder_exists(output_folder, input_folder)
    file_extension = filename.lower().split('.')[-1]
    supported_formats = ['png', 'jpg', 'jpeg', 'bmp', 'dib', 'jp2', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']
    if file_extension in supported_formats:
        input_path = os.path.join(input_folder, filename)
        analyzer = BorderAnalyzer()
        cropper = ImageCropper()
        left_border, right_border, top_border, bottom_border = analyzer.find_borders(input_path)

        if left_border is not None and right_border is not None and top_border is not None and bottom_border is not None:
            cropper.crop_image(input_path, left_border, right_border, top_border, bottom_border, output_folder, target_width, target_height)

if __name__ == "__main__":
    input_folder = "book"  # Replace with your folder
    # output_folder = "cropped_book"  # Optional; replace with your output folder
    # target_width = 1900  # Optional; set to None to disable resizing
    # target_height = 2782  # Optional; set to None to disable resizing

    # Using ThreadPoolExecutor to process images in parallel
    with ThreadPoolExecutor() as executor:
        for filename in os.listdir(input_folder):
            executor.submit(process_image, filename, input_folder, output_folder=None, target_width=None, target_height=None)
