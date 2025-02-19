from PIL import Image
import os
import img2pdf
import re

def natural_sort_key(s):
    """Hàm giúp sắp xếp theo thứ tự tự nhiên (1, 2, 10 thay vì 1, 10, 2)"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def process_image(image_path):
    # Mở ảnh với Pillow
    img = Image.open(image_path).convert('L')  # Chuyển sang grayscale
    return img

def save_images_to_pdf(folder_path, output_pdf):
    images = []
    temp_images = []
    
    # Lấy danh sách file và sắp xếp theo thứ tự tự nhiên
    files = sorted(os.listdir(folder_path), key=natural_sort_key)
    
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, file)
            processed_img = process_image(img_path)
            temp_path = img_path + "_processed.jpg"
            processed_img.save(temp_path)
            temp_images.append(temp_path)
            images.append(temp_path)
    
    # Xuất thành PDF
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))
    
    # Xóa ảnh tạm
    for temp_img in temp_images:
        os.remove(temp_img)

# Đường dẫn
folder_path = '/Users/kotori/Downloads/Sách luật'
output_pdf = '/Users/kotori/Downloads/Sách luật/output.pdf'
save_images_to_pdf(folder_path, output_pdf)