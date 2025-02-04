from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InfoFetcher():
    def __init__(self):
        self.driver = webdriver.Chrome()  # No need for executable_path

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")   
        
        # Find the search box and enter the query
        search_box = self.driver.find_element(By.NAME, "search")  # Use By.NAME to locate the search input
        search_box.send_keys(self.query + Keys.RETURN)  # Press Enter after entering the query
        #wait for the page to load
        time.sleep(1500)
        #search=self.driver.find_element_by_xpath()
        # Optionally, you could add more code here to scrape results

# Example usage
# assist = InfoFetcher()
# assist.get_info("hy")
