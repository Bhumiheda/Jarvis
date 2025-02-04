import requests

# API endpoint for fetching a random joke
url = "https://official-joke-api.appspot.com/random_joke"

def fetch_joke():
    try:
        # Fetch and parse the JSON response
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        json_data = response.json()
        
        # Extract the setup and punchline if available
        setup = json_data.get("setup", "No setup available")
        punchline = json_data.get("punchline", "No punchline available")
        
        # Return the joke as a formatted string
        return f"{setup} - {punchline}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the joke: {e}"

# Get and print the joke
joke = fetch_joke()
#print(joke)
