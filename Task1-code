from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.firefox.service import Service

# List of resolutions
resolutions = {
    "Desktop": ["1920x1080", "1366x768", "1536x864"],
    "Mobile": ["360x640", "414x896", "375x667"]
}

# Browsers to test
browsers = ["chrome", "firefox"]

# URL to test
url = "https://www.getcalley.com"


# Function to take screenshots
def take_screenshot(driver, device, resolution, page_name,browser):
    folder_path = os.path.join(os.getcwd(), device, resolution)
    os.makedirs(folder_path, exist_ok=True)
    screenshot_path = os.path.join(folder_path, f"{page_name}-{browser}-screenshot-{time.strftime('%Y%m%d-%H%M%S')}.png")
    driver.save_screenshot(screenshot_path)


# Function to navigate to each link
# Function to navigate to each link
def navigate_to_links(driver, device, resolution,browser):
    links = driver.find_elements(By.TAG_NAME, 'a')
    for i in range(5):
        # Refind the elements within the loop to avoid StaleElementReferenceException
        links = driver.find_elements(By.TAG_NAME, 'a')
        href = links[i].get_attribute('href')
        if href and href.startswith("http"):
            driver.get(href)
            page_name = href.split('/')[-1].split('.')[0]
            take_screenshot(driver, device, resolution, page_name,browser)
            time.sleep(2)


# Loop through resolutions and devices
for device, resolutions_list in resolutions.items():
    for resolution in resolutions_list:
        for browser in browsers:
            # Setup WebDriver
            driver = None
            if browser == "chrome":
                driver = webdriver.Chrome()
            elif browser == "firefox":

                driver = webdriver.Firefox()
            elif browser == "safari":
                driver = webdriver.Safari()

            # Maximize window for desktop resolutions
            if device == "Desktop":
                driver.maximize_window()
            # Set window size for mobile resolutions
            else:
                width, height = map(int, resolution.split('x'))
                driver.set_window_size(width, height)

            # Open URL
            driver.get(url)

            # Wait for page to load
            driver.implicitly_wait(20)

            # Navigate to each link and take screenshots
            navigate_to_links(driver, device, resolution, browser)

            # Close browser
            driver.quit()
