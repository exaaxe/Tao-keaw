<<<<<<< HEAD
from selenium import webdriver
import time 

# Set up the browser
browser = webdriver.Chrome()

# Open YouTube
browser.get("https://www.youtube.com/")

# Search for "Red Sun in the Sky"
search_box = browser.find_element_by_name("search_query")
search_box.send_keys("Red Sun in the Sky")
search_box.submit()

# Click on the first video in the search results
video = browser.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
video.click()


=======
from selenium import webdriver
import time 

# Set up the browser
browser = webdriver.Chrome()

# Open YouTube
browser.get("https://www.youtube.com/")

# Search for "Red Sun in the Sky"
search_box = browser.find_element_by_name("search_query")
search_box.send_keys("Red Sun in the Sky")
search_box.submit()

# Click on the first video in the search results
video = browser.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
video.click()


>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
