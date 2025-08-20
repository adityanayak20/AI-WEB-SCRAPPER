from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def scrape_website(website):
    print("Setting up Chrome options for local execution...")
    options = webdriver.ChromeOptions()
    
    chrome_args = os.getenv("SELENIUM_CHROME_ARGS")
    if chrome_args:
        for arg in chrome_args.split():
            options.add_argument(arg)
    
    options.binary_location = os.getenv("CHROME_BIN")
    
    print("Connecting to local Chromium...")
    # Use ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(website)
        print(f"Navigated to {website}! Scraping page content...")
        html = driver.page_source
        return html
    finally:
        driver.quit()
        print("Browser session closed.")

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]