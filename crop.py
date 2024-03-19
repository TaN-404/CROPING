from PIL import Image
import os

def crop_image(input_path, output_path, crop_rectangle):
    with Image.open(input_path) as img:
        cropped_img = img.crop(crop_rectangle)
        cropped_img.save(output_path)
    return output_path


input_path = 'input_imgs'

output_path = 'output_imgs'

# Define the crop_rectangle (left, upper, right, lower).
crop_rectangle = (40, 163, 1260, 879)

for filename in os.listdir('input_imgs'):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        input_path = os.path.join('input_imgs', filename)
        output_path = os.path.join('output_imgs', f'cropped_{filename}')
        crop_image(input_path, output_path, crop_rectangle)
        print(f'Cropped image saved to: {output_path}')
