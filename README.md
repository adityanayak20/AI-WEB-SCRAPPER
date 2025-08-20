# 🏠 AI Web Scraper (Selenium + LangChain + Streamlit)

This project scrapes property listings from a given URL (e.g., [PropertyFinder.ae](https://www.propertyfinder.ae)), then uses **LangChain + Ollama (LLaMA model)** to parse and organize the scraped content into a structured table.  
The data is shown in a **Streamlit web UI** where you can interact with the results.

---

## 📂 Project Structure

- **`Dockerfile`** – Defines the runtime environment, installs Python + required packages.  
- **`docker-compose.yml`** – Orchestrates services:  
  - `scraper` → Runs Streamlit app.  
  - `ollama` → Runs Ollama model backend.  
- **`run.sh`** – One-command build & run script for the whole project.  
- **`main.py`** – Streamlit frontend (user inputs + display).  
- **`scrape.py`** – Scraping logic (fetches raw HTML, extracts useful sections).  
- **`parse.py`** – Parsing helpers (turn HTML → structured rows of data).  

---

## ⚙️ Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) installed  
- ~5 GB free space (Ollama model `llama3:latest` will be pulled automatically the first time)  

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/adityanayak20/AI-WEB-SCRAPPER.git
   cd <repo-folder>

	2.	Make the run script executable

chmod +x run.sh


	3.	Start the project

./run.sh

This will:
	•	Build the Docker image
	•	Start ollama and scraper containers
	•	Launch the Streamlit app

	4.	Open the UI
Navigate to: http://localhost:8501

⸻

🎛️ Using the App

The UI has three input fields:
	1.	Page URL
Paste the property search page URL. Example:

https://www.propertyfinder.ae/en/search?l=733&c=2&fu=0&rp=y&ob=mr


	2.	Ask the AI about this page (free-text prompt)
Example prompts:

Can you please collect all of the relevant property information and organize it in a table.

Can you please collect all of the relevant property information and organize it in a table. And Please give the complete data as much possible


	3.	Ollama model
Default is:

llama3:latest



⸻

🖥️ Example Workflow
	1.	Start the app with ./run.sh.
	2.	Open http://localhost:8501.
	3.	Paste your property search URL.
	4.	Enter a natural language prompt (e.g., “Summarize all listings in a table”).
	5.	Select llama3:latest.
	6.	Click Scrape & Ask.
	7.	View the AI-generated table of property listings 🎉

⸻

📦 Output
	•	The scraped + parsed listings are displayed in the UI as a structured table.
	•	You can copy/paste or export results directly from Streamlit.

⸻

🛠️ Notes
	•	The first run may take longer because the LLaMA model (~4–5 GB) will be downloaded.
	•	The model is cached by Ollama and reused for future runs (across other AI projects too).
	•	Ethical scraping: respect target websites’ terms of service and add delays if scaling up.

⸻