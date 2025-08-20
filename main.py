import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


def get_driver():
    opts = Options()

    # Set Chrome binary path
    opts.binary_location = "/usr/bin/chromium"

    # Docker-optimized Chrome arguments
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-features=VizDisplayCompositor")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-plugins")
    opts.add_argument("--disable-images")
    opts.add_argument("--disable-javascript")
    opts.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")

    # Use system chromedriver
    service = Service("/usr/bin/chromedriver")

    return webdriver.Chrome(service=service, options=opts)


st.title("AI Web Scraper (Selenium + LangChain)")

url = st.text_input("Page URL")
prompt = st.text_area("Ask the AI about this page")
model_name = st.text_input("Ollama model", value="llama3:latest")

if st.button("Scrape & Ask") and url and prompt:
    with st.spinner("Fetching page..."):
        try:
            driver = get_driver()
            driver.get(url)
            html = driver.page_source
            driver.quit()

            soup = BeautifulSoup(html, "lxml")
            text = soup.get_text(separator="\n", strip=True)

            llm = ChatOllama(model=model_name)
            tmpl = ChatPromptTemplate.from_messages(
                [
                    ("system", "Answer based only on the provided page content."),
                    ("human", "Page content:\n{content}\n\nQuestion: {q}"),
                ]
            )

            chain = tmpl | llm
            resp = chain.invoke({"content": text[:200000], "q": prompt})

            st.subheader("Answer")
            st.write(resp.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")
