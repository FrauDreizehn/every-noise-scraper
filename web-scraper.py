import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime

def scrape_everynoise():
    # URL of the website
    url = "https://everynoise.com/"
    
    # Send GET request to the website
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: Status code {response.status_code}")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all genre divs
    genre_divs = soup.find_all('div', class_='genre')
    
    # List to store the results
    genres_data = []
    
    # Regular expression to extract artist and song from title
    pattern = r'e\.g\. (.*?) "(.+?)"'
    
    for div in genre_divs:
        genre = div.text.strip().replace('»', '').strip()  # Remove the '»' and extra spaces
        title = div.get('title', '')
        
        # Extract artist and song using regex
        match = re.search(pattern, title)
        if match:
            artist = match.group(1)
            song = match.group(2)
            
            genres_data.append({
                'genre': genre,
                'artist': artist,
                'song': song
            })
    
    return genres_data

def save_to_files(data):
    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save as JSON
    json_filename = f"everynoise_genres_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {json_filename}")
    
    # Save as readable text file
    txt_filename = f"everynoise_genres_{timestamp}.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write(f"Every Noise Genres - Scraped on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="* 50 + "\n\n")
        for item in data:
            f.write(f"Genre: {item['genre']}\n")
            f.write(f"Artist: {item['artist']}\n")
            f.write(f"Song: {item['song']}\n")
            f.write("-"* 30 + "\n")
    print(f"Data saved to {txt_filename}")

def main():
    # Scrape the data
    results = scrape_everynoise()
    
    if results:
        print(f"Found {len(results)} genres")
        # Save the results to files
        save_to_files(results)

if __name__ == "__main__":
    main()
