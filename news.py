import requests

# Replace with your actual API key
API_KEY = "81cc29cce7a448aca817e6223a03254a"
api_address = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# Fetch and parse the JSON data
try:
    response = requests.get(api_address)
    response.raise_for_status()  # Raise an error for bad responses
    json_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    json_data = None

def news():
    articles_list = []
    if json_data and "articles" in json_data:
        for i in range(min(3, len(json_data["articles"]))):  # Display up to 3 articles
            title = json_data["articles"][i].get("title", "No title available")
            articles_list.append(f"Number {i + 1}: {title}")
    else:
        print("No articles found or an error occurred.")
    return articles_list

# Call the function and print the news
# articles = news()
# print("\n".join(articles))