import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Selenium WebDriver
driver = webdriver.Chrome(executable_path="/path/to/your/selenium/driver")  # Update this path

# Website URL to visit
URL = "https://example.com"  # Replace with the desired website

def perform_random_text_selection(driver):
    """
    Randomly select and highlight visible text on the webpage.
    """
    try:
        # Find all elements containing text
        text_elements = driver.find_elements(By.XPATH, "//*[text()]")
        print(f"Found {len(text_elements)} text elements.")

        # Filter visible elements
        visible_text_elements = [elem for elem in text_elements if elem.is_displayed()]
        print(f"Found {len(visible_text_elements)} visible text elements.")

        if not visible_text_elements:
            print("No visible text elements found on the page.")
            return

        # Randomly choose a visible text element
        random_element = random.choice(visible_text_elements)

        # Scroll to the random element
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", random_element)

        # Highlight the selected element
        driver.execute_script("arguments[0].style.border='2px solid red';", random_element)
        print(f"Highlighted text: {random_element.text.strip()}")

        # Simulate hovering or clicking
        action = ActionChains(driver)
        action.move_to_element(random_element).perform()
        print("Hovered over the random text element.")

    except Exception as e:
        print(f"Error during random text selection: {e}")

def visit_and_select_text(driver, url):
    """
    Visit a website, wait for it to load, and perform random text selection.
    """
    try:
        # Open the website
        driver.get(url)
        print(f"Navigating to {url}...")
        
        # Wait for the website to load completely
        time.sleep(10)

        # Perform random text selection
        perform_random_text_selection(driver)
    except Exception as e:
        print(f"Error while visiting {url}: {e}")

def revisit_website(driver, url):
    """
    Revisit the website at random intervals and perform random text selection.
    """
    try:
        while True:
            # Visit and select text
            visit_and_select_text(driver, url)

            # Wait for a random interval between 6 and 24 hours
            wait_time = random.randint(6 * 3600, 24 * 3600)  # Convert hours to seconds
            print(f"Waiting for {wait_time // 3600} hours and {wait_time % 3600 // 60} minutes before the next visit...")
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("Revisiting stopped by user.")
    except Exception as e:
        print(f"Error during revisiting: {e}")

if __name__ == "__main__":
    try:
        # Start revisiting the website
        revisit_website(driver, URL)
    except Exception as e:
        print(f"Error during script execution: {e}")
    finally:
        # Close the browser
        driver.quit()
