from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get('https://dicionario.priberam.org/detrimento')

# Optionally, wait for some dynamic content to load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example of waiting for an element to be visible
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'some-dynamic-content'))
)

# Access the content
content = driver.page_source

# Do something with the content
print(content)

# Clean up, close the browser
driver.quit()
