FROM python:3.11-slim

ARG DEBIAN_FRONTEND=noninteractive

# Install system dependencies including chromium and chromedriver from same repo
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Python dependencies
RUN pip install --no-cache-dir \
    streamlit \
    selenium \
    beautifulsoup4 \
    lxml \
    html5lib \
    langchain \
    langchain-ollama \
    python-dotenv

WORKDIR /app
COPY . /app

EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
