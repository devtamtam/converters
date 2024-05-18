import os
import sys
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def get_image_files(directory):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    return [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]

def combine_images_to_pdf(directory, output_pdf):
    image_files = get_image_files(directory)
    
    if not image_files:
        print("No image files found in the directory.")
        return

    c = canvas.Canvas(output_pdf, pagesize=letter)
    
    for image_file in image_files:
        img_path = os.path.join(directory, image_file)
        img = Image.open(img_path)
        width, height = img.size
        c.setPageSize((width, height))
        c.drawImage(img_path, 0, 0, width, height)
        c.showPage()

    c.save()
    print(f"Combined {len(image_files)} images into {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python combine_images_to_pdf.py <output pdf>")
        sys.exit(1)

    output_pdf = sys.argv[1]
    current_directory = os.getcwd()
    
    combine_images_to_pdf(current_directory, output_pdf)
