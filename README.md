🏠 AI Web Scraper (Selenium + LangChain + Streamlit)

Scrapes a property search page (e.g., PropertyFinder.ae), then uses LangChain + an Ollama model to structure the results into a table—viewable in a Streamlit UI.

Files — what does what
	•	Dockerfile – Builds the Python runtime and installs project dependencies.
	•	docker-compose.yml – Starts the Streamlit app (scraper service) and Ollama.
	•	run.sh – One-command build + run helper.
	•	main.py – Streamlit UI (inputs, button, results table).
	•	scrape.py – Scraper logic (fetches/cleans HTML content).
	•	parse.py – Parsing helpers for turning raw HTML into structured data.

UI Input Parameters
	•	Page URL
Example:

https://www.propertyfinder.ae/en/search?l=733&c=2&fu=0&rp=y&ob=mr


	•	Ask the AI about this page (free-text prompt)
Examples:

Can you please collect all of the relevant property information and organize it in a table.

or

Can you please collect all of the relevant property information and organize it in a table. And Please give the complete data as much possible


	•	Ollama model
Example:

llama3:latest



How to run

chmod +x run.sh
./run.sh

Then open: http://localhost:8501