from selenium import webdriver
import time

# Initialize the WebDriver (provide the path to your Chrome WebDriver)
driver = webdriver.Chrome()
# Open the YouTube website
driver.get("https://www.youtube.com")

# Find the search input field by name
search_box = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")

# Enter your search query
search_query = "Python tutorial"  # Replace with the video you want to play
search_box.send_keys(search_query)

# Submit the search query
search_box.submit()

# Wait for search results to load (you can adjust the time as needed)
time.sleep(5)

# Click on the first search result (you can modify this to click on a specific video)
video_element = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
video_element.click()

# Wait for the video to load and start playing
time.sleep(4)
try:
    # Find the "like" button and click it (if it exists)
    like_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
    like_button.click()
except Exception as e:
    print("No 'like' button found or encountered an error:", e)
try:
    # Find the "Share" button (you may need to inspect the HTML to locate the right element)
    share_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")

    # Click the "Share" button
    share_button.click()

    # Wait for a few seconds to allow the share dialog to appear (adjust as needed)
    time.sleep(2)
except Exception as e:
    print("Unable to click the 'Share' button or encountered an error:", e)







# Wait for the like to be processed (you can adjust the time as needed)
time.sleep(5)
# You can add additional actions here, such as controlling playback, extracting information, or interacting with the video player

# Close the browser when done
driver.quit()
