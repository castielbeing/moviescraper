import requests
from bs4 import BeautifulSoup
import re

def search_and_choose_show(search_query):
    search_url = f"https://fmoviesz.to/filter?keyword={search_query.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links with /tv/ in the href attribute
    links = soup.find_all(href=re.compile(r'/tv/'))

    # Display search results with numbers, filtering out results that don't contain search words
    print("Search Results:")
    valid_links = []
    index = 1
    for link in links:
        title = link.text.strip()
        if all(word.lower() in title.lower() for word in search_query.split()):
            valid_links.append(link)
            print(f"{index}. {title}")
            index += 1

    # Ask the user to choose a result
    try:
        choice = int(input("Enter the number corresponding to the show you want to watch: "))
        selected_link = valid_links[choice - 1].get("href")
        show_url = f"https://fmoviesz.to{selected_link}"
        print(f"Opening {show_url}...")
        # Here, you can navigate to the selected show URL (show_url) using the web browser library or any other method you prefer.
        # For example, you can use the webbrowser library:
        # import webbrowser
        # webbrowser.open(show_url)
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

# Example usage
search_query = input("Enter search query: ")
search_and_choose_show(search_query)
