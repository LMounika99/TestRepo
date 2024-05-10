from selenium import webdriver
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test setup
URL = "https://demo.dealsdray.com/"
USERNAME = "prexo.mis@dealsdray.com"
PASSWORD = "prexo.mis@dealsdray.com"
SCREENSHOT_OUTPUT_PATH = "final_output_screenshot.png"

# Set up WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

# Open the URL
driver.get(URL)

# Log in
username_field = driver.find_element(By.XPATH, "//input[@id='mui-1']")
password_field = driver.find_element(By.XPATH, "//input[@id='mui-2']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]/button[1]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Add Bulk Orders']").click()

upload_button = driver.find_element(By.XPATH,
                                    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]")
upload_button.send_keys("C:\\Users\\pc\\PycharmProjects\\pythonProject6\\demo-data.xlsx")
if upload_button.get_attribute("value") == "":
    print("No file selected for upload")

    # Provide the file path

# Upload XLS file
driver.find_element(By.XPATH, "//button[normalize-space()='Import']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Validate Data']").click()

try:
    # Wait for the alert to be present
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert1 = driver.switch_to.alert
    alert1.accept()

    print("Alert accepted successfully")
except TimeoutException:
    print("Alert not present within timeout")
except NoAlertPresentException:
    print("No alert present")

# Capture screenshot of the final output page
driver.save_screenshot(SCREENSHOT_OUTPUT_PATH)
order_ids = []
imei_numbers = []
tracking_ids = []

table_rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
for row in range(1, len(table_rows) + 1):
    order_id = driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[2]").text.strip()
    imei_number = driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[12]").text.strip()
    tracking_id = driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[17]").text.strip()

    order_ids.append(order_id)
    imei_numbers.append(imei_number)
    tracking_ids.append(tracking_id)

# Validation
validation_passed = True

# Check for duplicate order IDs and IMEI numbers
if len(order_ids) != len(set(order_ids)):
    print("Validation failed: Duplicate order IDs found.")
    validation_passed = False

if len(imei_numbers) != len(set(imei_numbers)):
    print("Validation failed: Duplicate IMEI numbers found.")
    validation_passed = False

# Check for tracking IDs less than or equal to 12 digits
for tracking_id in tracking_ids:
    if len(tracking_id) <= 12:
        print("Validation failed: Tracking ID should be greater than 12 digits:", tracking_id)
        validation_passed = False

# Report validation results
if validation_passed:
    print("Validation passed! No duplicate order IDs or IMEI numbers, and all tracking IDs are greater than 12 digits.")
else:
    print("Validation failed! Please check the data for discrepancies.")

# Quit WebDriver
driver.quit()
