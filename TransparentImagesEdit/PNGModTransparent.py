import os
from PIL import Image

# Define folders
input_folder = "pics"
output_folder = "pics_transparent"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open image in RGBA mode
        image = Image.open(input_path).convert("RGBA")
        pixels = image.load()

        width, height = image.size

        # # Change white pixels to transparent
        # for x in range(width):
        #     for y in range(height):
        #         r, g, b, a = pixels[x, y]
        #         if (r, g, b) == (255, 255, 255):
        #             pixels[x, y] = (255, 255, 255, 0)  # Make white pixel transparent
        # Change near-white pixels to transparent (with tolerance)
        tolerance = 240
        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if r >= tolerance and g >= tolerance and b >= tolerance:
                    pixels[x, y] = (255, 255, 255, 0)  # Make near-white pixel transparent

        # Save the modified image
        image.save(output_path)
        print(f"Processed: {filename}")

print("✅ All images processed.")
