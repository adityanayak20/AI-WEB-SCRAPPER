⸻

🏠 AI Web Scraper (Selenium + LangChain + Streamlit)

This project scrapes property listings from PropertyFinder.ae, processes the data with AI (via Ollama), and provides an interactive web UI built with Streamlit.

⸻

📂 Project Structure
	•	Dockerfile → Defines the environment for the scraper (Python + dependencies).
	•	docker-compose.yml → Orchestrates services:
	•	scraper → Runs the Streamlit web app.
	•	ollama → Provides the LLaMA model backend for AI queries.
	•	main.py → Streamlit app (frontend UI for input + AI responses).
	•	scrape.py → Handles Selenium scraping logic (fetches property data).
	•	parse.py → Cleans and structures scraped HTML into a table format.
	•	run.sh → Helper script to build and run everything in one command.

⸻

▶️ How to Run
	1.	Make script executable (first time only):

chmod +x run.sh


	2.	Run the project:

./run.sh


	3.	Open your browser at 👉 http://localhost:8501

⸻

🖥️ Web UI Inputs
	•	Page URL → PropertyFinder search link.
	•	Ask the AI → Question about the page (e.g., “Summarize the property prices”).
	•	Ollama Model → Choose LLaMA variant (default: llama3:latest).

⸻

✅ Output
	•	A structured table of property listings (price, location, bedrooms, bathrooms, etc).
	•	AI-powered insights from the scraped page.

⸻