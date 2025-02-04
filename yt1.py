from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Music:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()  # Ensure that your PATH is configured for `chromedriver`

    def get_info(self, query):
        self.query = query
        # Navigate to YouTube with the search query
        self.driver.get(url=f"https://www.youtube.com/results?search_query={query}")
        
        # Wait for the page to load and search results to appear
        try:
            # Wait until at least one video title appears
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "video-title"))
            )
            first_video = self.driver.find_element(By.ID, "video-title")
            print("Page loaded successfully.")
            
            # Click the first video to play it
            first_video.click()
        except Exception as e:
            print("An error occurred while loading the page:", e)
        
        # Keep the page open indefinitely until the user presses Enter
        input("Press Enter to close the browser...")

# Example usage
# assist = Music()
# assist.play("fire by bts")
