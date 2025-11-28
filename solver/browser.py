# solver/browser.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_page_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=chrome_options
    )

    driver.get(url)
    html = driver.page_source
    driver.quit()

    return html
