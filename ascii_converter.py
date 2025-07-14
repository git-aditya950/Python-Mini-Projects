from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except:
        print("❌ Unable to open image file.")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string into lines
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # Print or save output
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_image)

    print("\n✅ ASCII art written to ascii_art.txt!")

# 🔁 Replace with your image path
convert_image_to_ascii("320927.jpg")
