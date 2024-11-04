import os
import random
from datetime import datetime, timedelta
from PyPDF2 import PdfWriter

# Directory to store the generated PDF files
dir_path = 'gen_pdfs'

# Function to create an empty PDF file
def create_empty_pdf(file_path):
    pdf_writer = PdfWriter()  # Create a PdfWriter object
    with open(file_path, 'wb') as pdf_file:
        pdf_writer.write(pdf_file)  # Write an empty PDF

# Function to set random modification time for the file
def set_random_modification_time(file_path):
    # Generate a random date in the past year
    start_date = datetime.now() - timedelta(days=365)
    random_date = start_date + timedelta(days=random.randint(0, 365), 
                                         hours=random.randint(0, 23), 
                                         minutes=random.randint(0, 59))

    # Convert the random date to a timestamp
    mod_time = random_date.timestamp()
    
    # Set both access and modification times to the random time
    os.utime(file_path, (mod_time, mod_time))

# Generate 200 empty PDF files with random dates
for i in range(200):
    file_name = f"file_{i + 1}.pdf"
    file_path = os.path.join(dir_path, file_name)
    
    # Create an empty PDF file
    create_empty_pdf(file_path)
    
    # Set a random modification time
    set_random_modification_time(file_path)

    print(f"Created {file_name} with random modification time.")
