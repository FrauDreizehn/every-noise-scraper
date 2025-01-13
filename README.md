# every-noise-scraper

Description

The EveryNoise Genre Scraper is a Python script that extracts music genres and their representative artists from the website www.everynoise.com. This tool is useful for music enthusiasts, researchers, and developers who want to analyze or visualize the diversity of music genres and their associated artists.

Features

  Genre Extraction: Scrapes all music genres listed on EveryNoise.
  Artist Representation: Retrieves a representative artist for each genre.
  Data Storage: Saves the scraped data in a structured format (e.g., TXT or JSON).
  Error Handling: Includes basic error handling for network requests and data parsing.

Requirements

  Python 3.x
  requests library for making HTTP requests
  BeautifulSoup library for parsing HTML
  pandas library for data manipulation (optional, for CSV export)

You can install the required libraries using pip:

    pip install requests beautifulsoup4 pandas

Usage

Clone the repository:

    git clone https://github.com/yourusername/everynoise-genre-scraper.git
    cd everynoise-genre-scraper

Run the script:

    python everynoise_scraper.py

    The scraped data will be saved in a file named genres_artists.csv.

Example

The scraper will extract genres such as "Rock", "Pop", "Jazz", etc., along with a representative artist for each genre, like "The Beatles" for Rock or "Taylor Swift" for Pop.
