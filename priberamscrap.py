import requests
from bs4 import BeautifulSoup

def fetch_definitions(term):
    url = f"https://dicionario.priberam.org/{term}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    definitions = []
    idiomatic_expressions = []

    # Extracting definitions
    definition_section = soup.find_all('p', class_='dp-definicao-linha')
    for definition in definition_section:
        text = definition.get_text(strip=True, separator=' ')
        definitions.append(text)

    # Extracting idiomatic expressions
    idiomatic_section = soup.find_all('h4', id=lambda x: x and x.startswith('agulha'))
    for expression in idiomatic_section:
        expression_text = expression.get_text(strip=True)
        description = expression.find_next('p').get_text(strip=True, separator=' ')
        idiomatic_expressions.append(f"{expression_text}: {description}")

    return definitions, idiomatic_expressions

# Example usage for multiple terms
terms = ["agulha", "casa"]
for term in terms:
    definitions, idiomatic_expressions = fetch_definitions(term)
    print(f"Definitions for {term}:")
    for definition in definitions:
        print(definition)
    print("\nIdiomatic Expressions for {term}:")
    for expression in idiomatic_expressions:
        print(expression)
    print("\n" + "-"*50 + "\n")
