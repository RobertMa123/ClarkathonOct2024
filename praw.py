from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Function to search YouTube channels using Selenium and BeautifulSoup
def search_youtube_channels(keyword):
    # Initialize the Selenium WebDriver using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open YouTube search with the given keyword
    search_url = f"https://www.youtube.com/results?search_query={keyword}+channel"
    driver.get(search_url)

    # Wait for the page to load completely
    time.sleep(5)

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    channels = soup.find_all('a', href=True, class_='yt-simple-endpoint style-scope ytd-channel-name')

    # Check if any channels were found
    if not channels:
        print("No channels found. Please try a different keyword.")
        driver.quit()
        return

    # Extract and print channel names and URLs
    for channel in channels:
        channel_name = channel.text.strip()
        channel_url = "https://www.youtube.com" + channel['href']

        # Ensure we are only capturing channel URLs (not videos or other links)
        if '/channel/' in channel_url or '/user/' in channel_url:
            print(f"Channel: {channel_name}, URL: {channel_url}")

    driver.quit()

keyword = input("Enter a keyword to search for YouTube channels: ")

search_youtube_channels(keyword)
