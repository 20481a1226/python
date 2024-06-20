import requests
from bs4 import BeautifulSoup

# Define the URL of the news website
url = "https://www.example.com/news/article123"  # Replace with the actual URL

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find the news article element (replace with appropriate selector for the website)
  article = soup.find('div', class_='article-content')  # Adjust the selector as needed

  # Extract the title (replace with appropriate class/id if different)
  title = article.find('h1', class_='article-title').text.strip()

  # Extract the body text (replace with appropriate selector if different)
  body = article.find('p', class_='article-body').text.strip()

  # Print the extracted data
  print("Title:", title)
  print("Body:", body)
else:
  print("Error: Failed to retrieve the article.")

