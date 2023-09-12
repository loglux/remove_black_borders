import cv2
import os
import numpy as np


class BorderAnalyzer:
    def __init__(self, white_threshold=245):
        self.white_threshold = white_threshold

    def find_borders(self, img_path):
        img = cv2.imread(img_path)
        if img is None:
            print("Image not found.")
            return None, None

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        left_border = 0
        right_border = w - 1

        for i in range(w):
            col = gray[:, i]
            if np.mean(col) > self.white_threshold:
                left_border = i
                break

        for i in range(w - 1, -1, -1):
            col = gray[:, i]
            if np.mean(col) > self.white_threshold:
                right_border = i
                break

        return left_border, right_border


class ImageCropper:
    def crop_image(self, img_path, left, right, output_folder, target_width=None, target_height=None):
        img = cv2.imread(img_path)
        if img is None:
            print("Image not found.")
            return

        cropped_img = img[:, left:right]

        # Resize the image only if target dimensions are specified
        if target_width and target_height:
            cropped_img = cv2.resize(cropped_img, (target_width, target_height))

        output_path = os.path.join(output_folder, os.path.basename(img_path))
        cv2.imwrite(output_path, cropped_img)

        if target_width and target_height:
            print(f"Saved cropped and resized image to {output_path}")
        else:
            print(f"Saved cropped image to {output_path}")


if __name__ == "__main__":
    input_folder = "book"  # Replace with your folder
    output_folder = "cropped_book"  # Replace with your output folder
    # target_width = 1900  # Optional; set to None to disable resizing
    # target_height = 2782  # Optional; set to None to disable resizing

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    analyzer = BorderAnalyzer()
    cropper = ImageCropper()

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            left_border, right_border = analyzer.find_borders(input_path)

            if left_border is not None and right_border is not None:
                cropper.crop_image(input_path, left_border, right_border, output_folder, target_width=None, target_height=None)
