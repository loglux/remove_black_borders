# Image Border Detection and Cropping

This Python script is designed to detect and crop the borders of images stored in a specified folder. It can be useful for removing unwanted white or blank margins from scanned documents or images.

## Prerequisites

Before using this script, you need to have the following dependencies installed:

- OpenCV (cv2):
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

- The script will now process all the supported files in the input folder, detect and crop borders from all sides, and save the cropped images in the output folder.

## Customization

- The `white_threshold` parameter in the BorderAnalyzer class has been adjusted to 85 to enhance the detection of lighter-coloured borders. You can further customize this threshold to better suit your images' characteristics.
- In image processing, pixel values typically range from 0 to 255, where 0 represents black and 255 represents white. The `white_threshold` parameter is used to determine how light a pixel must be to be considered part of a white border. For example, `white_threshold` value closer to 255 would make the script more sensitive to white and very light colours.

## Example

In the provided script, the default `input_folder` is set to "book," and the default `output_folder` is set to "cropped_book." You can replace these values with your own folder paths.

```python
input_folder = "your_input_folder"
output_folder = "your_output_folder"
```

Please replace `"your_input_folder"` and `"your_output_folder"` with the actual folder paths you want to use. 

## License
This script is licensed under the MIT License.