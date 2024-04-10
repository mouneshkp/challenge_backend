import requests
from bs4 import BeautifulSoup
import json

def perform_google_search(query: str) -> str:
    base_url = 'https://www.google.com/search'
    params = {'q': query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()
    return response.text

def parse_search_results(html_content: str):
    soup = BeautifulSoup(html_content, 'html.parser')
    results = []
    for result in soup.select('.tF2Cxc'):
        title = result.select_one('h3').text if result.select_one('h3') else 'No Title'
        link = result.select_one('a')['href'] if result.select_one('a') else 'No Link'
        description = result.select_one('.IsZvec').text if result.select_one('.IsZvec') else 'No Description'
        results.append({
            'title': title,
            'link': link,
            'details': description
        })
        if len(results) == 10:
            break
    return results

def main():
    query = "finkraft"
    html_content = perform_google_search(query)
    results = parse_search_results(html_content)
    
    if results:
        with open("results.json", "w", encoding="utf-8") as json_file:
            json.dump(results, json_file, indent=4)
        for result in results:
            print(result)
    else:
        print("No results found, check the HTML output for changes.")
        with open("debug_output.html", "w", encoding="utf-8") as f:
            f.write(html_content)

if __name__ == "__main__":
    main()
