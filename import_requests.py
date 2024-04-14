import requests
import pandas as pd

words_df = pd.read_csv('/Users/josephpereira/medport/port_terms_test.csv', encoding='ISO-8859-1')
api_url = "http://api.dicionario-aberto.net/word/"
flashcards_data = []

for word in words_df['word']:
    try:
        response = requests.get(api_url + word)
        if response.status_code == 200:
            data = response.json()
            if data:
                entry_xml = data[0]['xml']
                # Further processing here...
                print(f"Success for word '{word}'")
            else:
                print(f"No data found for word '{word}'")
        else:
            print(f"API request failed for word '{word}' with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred for word '{word}': {e}")

