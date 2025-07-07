from PIL import Image

def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"✅ Image saved as {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Input from user
input_path = input("📁 Enter path of the image: ").strip()
output_path = input("💾 Enter output image name (e.g., resized.jpg): ").strip()
width = int(input("📏 Enter new width (in px): "))
height = int(input("📏 Enter new height (in px): "))

resize_image(input_path, output_path, width, height)
