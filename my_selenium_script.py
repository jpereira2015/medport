from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get('https://dicionario.priberam.org/detrimento')

# Wait for the specific section of the word to be visible on the page
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'article.pb-def')))

# Get the definition element within the specific section
definition_element = driver.find_element(By.CSS_SELECTOR, 'article.pb-def .dp-definicao')

# Extract and print the definitions
definitions = definition_element.find_elements(By.CSS_SELECTOR, '.dp-definicao-linha .def')
for definition in definitions:
    print(definition.text)

# Clean up, close the browser
driver.quit()
