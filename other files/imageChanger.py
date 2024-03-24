import base64
from PIL import Image
from io import BytesIO
import os

# Decode and save the image
base64_data = "your_base64_string"
image_data = base64.b64decode(base64_data)
image = Image.open(BytesIO(image_data))
image_path = "weather_icon.png"
image.save(image_path)

# Check if the file is saved
if os.path.exists(image_path):
    print("Image saved successfully.")
else:
    print("Failed to save the image.")