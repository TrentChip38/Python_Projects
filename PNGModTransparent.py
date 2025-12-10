import os
from PIL import Image

# Define folders
input_folder = "DiceSymbols"
output_folder = "DiceSymbols_Modified"

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

        # Change visible black pixels to white
        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if a > 0:#(r, g, b) == (0, 0, 0) and
                    pixels[x, y] = (255, 255, 255, a)

        # Save the modified image
        image.save(output_path)
        print(f"Processed: {filename}")

print("✅ All images processed.")
