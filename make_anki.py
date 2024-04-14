import pandas as pd
import csv

# Load your data from a CSV file
# Replace '/path/to/your/data.csv' with the actual path to your CSV file
data_path = '/path/to/your/data.csv'
data = pd.read_csv(data_path)

html_recognition_flashcards = []

for index, row in data.iterrows():
    # Only proceed if there's an example sentence
    if pd.notnull(row['Example Sentence']):
        # Using HTML to bold the term
        # Make sure 'word' column exists in your DataFrame, adjust the column name if necessary
        front = row['Example Sentence'].replace(row['word'], f"<b>{row['word']}</b>")
        back = row['definition'] if pd.notnull(row['definition']) else "No definition provided"
        html_recognition_flashcards.append({"Front": front, "Back": back})

# Writing the HTML formatted recognition flashcards to a new CSV file
csv_file_path_html_recognition = '/mnt/data/medical_portuguese_html_recognition_flashcards.csv'

with open(csv_file_path_html_recognition, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Front", "Back"])
    writer.writeheader()
    for card in html_recognition_flashcards:
        writer.writerow(card)

# Display or return the path of the new CSV file
print(csv_file_path_html_recognition)
