import sys
from PIL import Image

def compress_image(filename):
    name, image_format = filename.split('.')
    image = Image.open(filename)
    image.save(f'{name}-min.{image_format}', quality=95, optimize=True)

if __name__ == '__main__':
    compress_image(sys.argv[1])
