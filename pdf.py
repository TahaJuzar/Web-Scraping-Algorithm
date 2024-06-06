import os
import requests
import pdfplumber
# List of PDF URLs
biology_books = [
    "https://download.library.lol/main/3255000/2209eb833b2cdfc54558febf2280f740/Richard%20Fosbery%2C%20Gareth%20Williams%20-%20Cambridge%20IGCSE%C2%AE%20%26%20O%20Level%20Essential%20Biology_%20Student%20Book-Oxford%20University%20Press%20%282021%29.pdf",  # o level
    "https://wisegot.com/wp-content/uploads/2022/03/Cambridge-International-AS-_-A-Level-Mary-Jones-bio-4.pdf",  # a level
    "https://www.taleem360.com/download/1st-year-biology-punjab-textbook-ebook-updated-edition-2kk",  # 1st-year-biology-punjab-textbook-ebook
    "https://www.taleem360.com/download/balochistan-board-11th-class-biology-text-book-pdf-qpl",  # balochistan board 11 biology book
    "https://invent.ilmkidunya.com/images/Section/Bio-12th-KPK.pdf",  # 12th-class/books/biology-kpk-board
    "https://drive.google.com/file/d/1PQMrP44cXssuI1OJDCPE1YPz4dhwi_sY/view",  # 12th biology punjab
    "https://invent.ilmkidunya.com/images/Section/10th-Class-Biology-English-Medium.pdf",  # 10th biology punjab
    "https://www.taleem360.com/download/kpk-board-10th-class-biology-text-book-pdf-w7t",  # 10th kpk biology
    "https://ebooks.stbb.edu.pk/storage/uploads/books/941344618.pdf",  # 9th class sindh board biology
    "https://drive.usercontent.google.com/download?id=1j-SRUikqm3-B1n71SfjPWAAfBEOgy0gk&export=download&authuser=0"  # 9th class biology punjab
]
# URL of the second PDF
url = biology_books[1]
# Directory where the file will be saved
save_directory = r"C:\Users\Yoga X380\Desktop\pdffiles_script"
file_name = "Cambridge-International-AS-A-Level-Mary-Jones-bio-4.pdf"
save_path = os.path.join(save_directory, file_name)
# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)
# Download the PDF
response = requests.get(url)
with open(save_path, 'wb') as file:
    file.write(response.content)
print(f"PDF downloaded and saved to {save_path}")
# Function to extract text from PDF
def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
# Extract text from the downloaded PDF
extracted_text = extract_text(save_path)
print(extracted_text)