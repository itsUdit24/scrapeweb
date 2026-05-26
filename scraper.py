import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print("\nQuote:", text)
    print("Author:", author)

    quotes_data.append({
        "Quote": text,
        "Author": author
    })

# Save to CSV
df = pd.DataFrame(quotes_data)

df.to_csv("quotes.csv", index=False)

print("\nData saved to quotes.csv")