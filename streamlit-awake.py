import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random

# Initialize Selenium WebDriver
driver = webdriver.Chrome(executable_path="/path/to/your/selenium/driver")  # Update path to your WebDriver

# Streamlit app URL
STREAMLIT_APP_URL = "https://<your-streamlit-app-url>.streamlit.app/"  # Replace with your app's URL

def wake_up_streamlit_app(driver):
    """
    Visits the Streamlit app, waits for it to load, clicks the wake-up button,
    and performs random scrolling.
    """
    # Navigate to the Streamlit app
    driver.get(STREAMLIT_APP_URL)
    print("Navigating to the Streamlit app...")

    # Wait for the page to load completely
    time.sleep(10)

    # Locate and click the "Wake Up" button
    try:
        wake_up_button = driver.find_element(By.XPATH, "//button[contains(text(), 'get the app back up and running')]")
        wake_up_button.click()
        print("Clicked the 'Wake Up' button.")
    except Exception as e:
        print(f"Error locating or clicking the 'Wake Up' button: {e}")

    # Perform random scrolling
    print("Performing random scrolling...")
    for _ in range(5):  # Scroll multiple times
        scroll_amount = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(1, 2))

def main():
    """
    Main function to run the wake-up task on a 24-hour loop.
    """
    while True:
        try:
            # Call the wake-up function
            wake_up_streamlit_app(driver)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Task completed. Waiting for 24 hours before the next run...")
            time.sleep(86400)  # Wait for 24 hours before the next iteration

if __name__ == "__main__":
    main()
