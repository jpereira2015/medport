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

        # Extract definitions
        definitions = soup.find_all("div", class_="dp-definicao")
        if definitions:
            print(f"Term: {word.capitalize()}")
            print("Definitions:")
            for definition in definitions:
                print(f"- {definition.find('div', class_='dp-definicao-cartao__descricao').text.strip()}")

        else:
            print("No definitions found")

        # Output idiomatic expressions and specific uses
        print("\nIdiomatic Expressions and Specific Uses:")
        expressions_list = ["agulha de marear", "agulha magnética", "procurar agulha em palheiro"]
        for expression in expressions_list:
            expression_tag = soup.find("a", {"name": expression})
            if expression_tag:
                description = expression_tag.find_next("div", class_="def").text.strip()
                print(f"{expression}: {description}")
            else:
                print(f"{expression}: No description found")

        # Optionally, find and output etymology
        etymology_section = soup.find("a", {"name": "etimologia"})
        if etymology_section:
            etymology = etymology_section.find_next("div", class_="def")
            if etymology:
                print("\nEtymology:")
                print(etymology.text.strip())
            else:
                print("No etymology found")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage for {word}: {e}")
    except Exception as e:
        print(f"An error occurred while fetching definitions for {word}: {e}")

# Example usage
fetch_definitions("agulha")
