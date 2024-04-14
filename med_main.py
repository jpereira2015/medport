import requests
import pandas as pd
import xml.etree.ElementTree as ET

# Load the list of words from your CSV, assuming it's in ISO-8859-1 encoding
words_df = pd.read_csv('/Users/josephpereira/medport/port_terms_utf8_file.csv', encoding='utf-8')

# Convert all words to lowercase for consistency
words_df['word'] = words_df['word'].str.lower()

api_url = "http://api.dicionario-aberto.net/word/"

# Prepare an empty list to hold the flashcard data
flashcards_data = []

# Fetch definitions for each word
for word in words_df['word']:
    response = requests.get(f"{api_url}{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            # Parse the first entry's XML to get the first definition
            entry_xml = data[0]['xml']
            root = ET.fromstring(entry_xml)
            definition = root.find(".//def").text if root.find(".//def") is not None else "NA"
            # Ensure that the definition is a string and handle any potential errors
            definition = str(definition).replace('\n', ' ').replace('"', "'")
            
            flashcards_data.append({
                'word': word,
                'definition': definition
            })
        else:
            flashcards_data.append({
                'word': word,
                'definition': "NA"
            })
    else:
        flashcards_data.append({
            'word': word,
            'definition': "NA"
        })

# Convert the list of data to a DataFrame
flashcards_df = pd.DataFrame(flashcards_data)

# Write the DataFrame to a new CSV file using UTF-8 encoding to ensure broad compatibility
flashcards_df.to_csv('/Users/josephpereira/medport/flashcards.csv', index=False, encoding='utf-8')


