# Image Border Detection and Cropping

This Python script is designed to detect and crop the borders of images stored in a specified folder. It can be useful for removing unwanted white or blank margins from scanned documents or images.

## Prerequisites

Before using this script, you need to have the following dependencies installed:

- OpenCV (cv2): A popular computer vision library for Python. You can install it using pip:
```bash
pip install opencv-python
```

## Usage

1. Clone or download this repository to your local machine.

2. Place the images you want to process in a folder of your choice. You can set the input folder by modifying the `input_folder` variable in the script.

3. Optionally, specify the output folder where the cropped images will be saved by modifying the output_folder variable in the script. If not provided, it defaults to a folder with the same name as the input folder but prefixed with "cropped_".

4. Optionally, you can set target dimensions for the cropped images by modifying the `target_width` and `target_height` variables. If you want to keep the original dimensions, set these variables to `None`.

5. Run the script:
```bash
python remove_black_borders.py
```

The script will process all the PNG files in the input folder, detect and crop the borders, and save the cropped images in the output folder.

## Customization

- You can customize the white threshold used for border detection by modifying the `white_threshold` parameter in the `BorderAnalyzer` class. This threshold determines what is considered "white" in the image.

## Example

In the provided script, the default `input_folder` is set to "book," and the default `output_folder` is set to "cropped_book." You can replace these values with your own folder paths.

```python
input_folder = "your_input_folder"
output_folder = "your_output_folder"
```

Please replace `"your_input_folder"` and `"your_output_folder"` with the actual folder paths you want to use. You can also provide additional information or customization instructions in the README as needed.

## License
This script is licensed under the MIT License.