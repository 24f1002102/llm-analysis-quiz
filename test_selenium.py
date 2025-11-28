from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs browser in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)

# Open a page to test
driver.get("https://example.com")
print("Page title:", driver.title)

driver.quit()
