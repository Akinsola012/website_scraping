Job Search Dashboard

A web application that scrapes job postings (titles, companies, locations, and metadata) from Indeed using Playwright, stores them in a SQLite database, analyzes job trends with Pandas, and visualizes insights using Matplotlib and Seaborn. Built with Streamlit, the dashboard provides interactive filters and real-time search capabilities. It’s deployed via Streamlit Cloud.

Features
- Scrapes job postings including title, company, location, job type, posted date, and rating
- Filters jobs by title, location, or company
- Searches job postings using keywords
- Visualizes job distribution by category and region
- Deployed at: (https://indeed-dashboard.streamlit.app/)

Scraping Strategy
- Playwright Automation
Uses async_playwright to control Chromium via CDP and extract structured job data directly from the DOM.
- Bypass Verification
Connects to a manual browser session with realistic headers and cookies to avoid CAPTCHAs or bot checks.
- Pagination Control
Automatically clicks “Next Page” and scrolls pages to dynamically load job listings across multiple pages.
- Location Switching
Queries jobs by state or region by modifying the location in the search URL.
- Field Inference
Derives remote_or_onsite and job_type status from keyword patterns in scraped job text.

Technologies Used
- Python 3.10
- Playwright (scraping)
- SQLite3 (local database)
- Pandas, Seaborn, Matplotlib (data analysis & visualization)
- Streamlit (dashboard UI)
- Streamlit Cloud (deployment)


Setup Instructions
# Clone the repository
git clone https://github.com/Akinsola012/website_scraping.git


# Install dependencies
pip install -r requirements.txt

# Run the scraper (manual Chrome must be open at port 9222)
python scraping.py  

# Run the dashboard locally
streamlit run streamlit_app.py


 Future Improvements
- Integrate salary scraping and normalize values for analysis
- Automate scraping tasks with:
- Prefect: for declarative Python scheduling
- Apache Airflow: for DAG-driven orchestration
- Windows Task Scheduler: for local automation
- Enable data export (CSV, Excel) from dashboard filters
- Add user authentication and access control

 Author

Created by Akinsola O.A


