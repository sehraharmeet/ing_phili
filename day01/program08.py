from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open site
driver.get("https://practicetestautomation.com/practice-test-login/")
# Step 2: Login
driver.find_element(By.ID, "username").send_keys("harmeet")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

time.sleep(0)

# Step 3: Scrape text/table content
message = driver.find_element(By.TAG_NAME, "h1").text
print("Page heading:", message)

content = driver.find_element(By.CLASS_NAME, "post-content").text
print("Page content:\n", content)

time.sleep(2)

# Step 4: Logout
driver.find_element(By.LINK_TEXT, "Log out").click()

print("Logged out successfully")

input("Press Enter to close...")
driver.quit()

