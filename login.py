from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    service = Service("C:\\Windows\\WebDriver\\chromedriver.exe")
    return webdriver.Chrome(service=service, options=options)

def wait_and_find_element(driver, by, value, timeout=20):
    """Utility function to wait for and find an element"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))

try:
    driver = setup_driver()
    wait = WebDriverWait(driver, 20)
    
    # Navigate to Instagram
    print("Navigating to Instagram...")
    driver.get("https://www.instagram.com/")
    time.sleep(5)  # Wait for page to load completely
    
    # Login with more reliable selectors
    print("Entering login credentials...")
    username_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='username']")))
    password_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='password']")))
    
    username_field.clear()
    username_field.send_keys("<__YOUR_PASSWORD_HERE__>")
    password_field.clear()
    password_field.send_keys("<__YOUR_PASSWORD_HERE__>") 
    
    # Click login button
    print("Clicking login button...")
    login_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    
    # Handle "Save Login Info" dialog
    time.sleep(5)
    try:
        save_info_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[role='button']:not([tabindex='-1'])")))
        save_info_button.click()
        print("Handled 'Save Login Info' prompt")
    except Exception as e:
        print("No 'Save Login Info' prompt found")
    
    # Handle "Turn on Notifications" dialog
    time.sleep(3)
    try:
        notifications_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button._a9--._a9_1")))
        notifications_button.click()
        print("Handled notifications prompt")
    except Exception as e:
        print("No notifications prompt found")
    
    print("Login sequence completed successfully!")
    
    # Keep browser open for verification
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")

finally:
    print("Script completed")
    # Uncomment the following line when you want the browser to close automatically
    driver.quit()
    
