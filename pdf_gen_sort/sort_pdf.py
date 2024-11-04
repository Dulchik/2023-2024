import os
from datetime import datetime

# Directory where the PDF files are located
dir_path = 'gen_pdfs'

# List only PDF files in the directory
pdf_files = [file for file in os.listdir(dir_path) if file.endswith('.pdf')]

# Sort files based on modification time
sorted_files = sorted(pdf_files, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

# Rename each file with its modification date
for file_name in sorted_files:
    file_path = os.path.join(dir_path, file_name)
    
    # Get the modification time
    mod_time = os.path.getmtime(file_path)
    
    # Convert the modification time to a human-readable format (YYYY-MM-DD)
    mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
    
    # Create the new filename with the modification date as a prefix
    new_file_name = f"{mod_date}_{file_name}"
    new_file_path = os.path.join(dir_path, new_file_name)
    
    # Rename the file
    os.rename(file_path, new_file_path)
    
    print(f"Renamed {file_name} to {new_file_name}")
