import fitz
import os
def extract_text_and_images(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    doc = fitz.open(pdf_path)
    # Extract text from each page
    for i in range(doc.page_count):
        page = doc.load_page(i)
        text = page.get_text()
        with open(os.path.join(output_folder, f"page_{i+1}_text.txt"), "w", encoding="utf-8") as text_file:
            text_file.write(text)
        print(f"Extracted text from page {i+1}")
    # Extract images from each page
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        pix.save(os.path.join(output_folder, f"page_{i+1}_image.png"))
        print(f"Extracted image from page {i+1}")
# Example usage:
pdf_path = "Cambridge-International-AS-_-A-Level-Mary-Jones-bio-4.pdf"
output_folder = "D:/py2/output"
extract_text_and_images(pdf_path, output_folder)