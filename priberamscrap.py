import requests
from bs4 import BeautifulSoup

def fetch_definitions(word):
    url = f"https://dicionario.priberam.org/{word.replace(' ', '%20')}"

    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract definitions, ensure only those under the right section
        definitions_section = soup.find("div", {"id": "contentorDefinicoes"})  # Assuming this is the correct container ID
        if definitions_section:
            definitions = definitions_section.find_all("p", class_="dp-definicao-linha")
            print(f"Term: {word.capitalize()}")
            print("Definitions:")
            for definition in definitions:
                text = ' '.join(definition.stripped_strings)
                print(text)
        else:
            print("No definitions found")

        # Output idiomatic expressions and specific uses, within the definitions section
        print("\nIdiomatic Expressions and Specific Uses:")
        expressions_list = ["agulha de marear", "agulha magnética", "procurar agulha em palheiro"]
        if definitions_section:
            for expression in expressions_list:
                expression_tag = definitions_section.find("h4", id=expression)
                if expression_tag:
                    description = expression_tag.find_next_sibling("span").text.strip() if expression_tag.find_next_sibling("span") else "No description available"
                    print(f"{expression}: {description}")
                else:
                    print(f"{expression}: No description found")

        # Optionally, find and output etymology, also within the definitions section
        if definitions_section:
            try:
                etymology = definitions_section.find("div", class_="my-12 dp-seccao-icon")
                if etymology:
                    etymology_text = ' '.join(etymology.stripped_strings)
                    print("\nEtymology:")
                    print(etymology_text)
                else:
                    print("No etymology found")
            except Exception as e:
                print(f"An error occurred while fetching etymology for {word}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage for {word}: {e}")
    except Exception as e:
        print(f"An error occurred while fetching definitions for {word}: {e}")

# Example usage
fetch_definitions("Agulha")
