import sys
from transform_image import transform_image_url

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_url>")
        sys.exit(1)
    
    image_url = sys.argv[1]
    try:
        new_image_url = transform_image_url(image_url)
        print(new_image_url)
    except ValueError as e:
        print(e)
        sys.exit(1)
