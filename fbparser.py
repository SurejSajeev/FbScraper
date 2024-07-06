from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scroll_down(driver):
    """Scroll down the page."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust sleep time as necessary to allow content to load


if __name__ == "__main__":

    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')  # Disable browser notifications
    options.add_argument('--disable-popup-blocking')
    service = Service("C:\\Users\\surej\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.facebook.com/')
    driver.find_element(By.ID, 'email').send_keys('surejsajeev@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Myfb@92')
    driver.find_element(By.NAME, 'login').click()

    time.sleep(5)  # Wait for the page to load
    driver.get('https://www.facebook.com/groups/117412174975402')

    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)


    def close_popup(xpath):
        """Function to close popup based on given XPath."""
        try:
            popup = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            popup.click()
            print(f"Popup closed: {xpath}")
        except Exception as e:
            print(f"No popup to close for XPath {xpath} or could not be closed. Exception: {e}")


    # Example: Close potential login popups
    # close_popup('//div[contains(@class, "login-popup-class")]//button[contains(@class, "close-button-class")]')
    # close_popup('//div[contains(@class, "other-popup-class")]//button[contains(@class, "close-button-class")]')

    # Example XPath with partial matching for dynamic content
    xpath_template = '//*[contains(@id, ":r")]/span/span/a/strong/span'
    context_template = '//*[contains(@id, ":r")]/div/div/span'
    see_more_template = '//*[contains(@id, ":r")]/div/div/span/div[3]/div/div'

    # Set to store unique elements
    elements_text_set = set()
    content_text_set = set()
    counter = 0
    # Scroll and search loop
    try:
        elements = driver.find_elements(By.XPATH, xpath_template)
        while True:
            # Find elements that match the XPath pattern
            elements = driver.find_elements(By.XPATH, xpath_template)
            # try:
            #     specific_element = wait.until(
            #         EC.element_to_be_clickable((By.XPATH, see_more_template)))
            #     specific_element.click()
            #     print("Clicked the specific element.")
            # except Exception as e:
            #     print(f"Specific element could not be clicked or was not present. Exception: {e}")

            # Extract and print text from found elements
            for element in elements:
                text = element.text
                if text not in elements_text_set:
                    elements_text_set.add(text)
                    print(f"Found text: {text}")
                    counter += 1
                    break

                try:
                    see_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "x1i10hfl") and text()="See more"]')))
                    see_more_button.click()
                    print("Clicked the 'See More' button.")
                except Exception as e:
                    print(f"'See More' button could not be clicked or was not present. Exception: {e}")

                wait.until(
                    EC.element_to_be_clickable((By.XPATH, context_template)))
                contents = driver.find_elements(By.XPATH, context_template)
                # driver.execute_script("arguments[0].scrollTo();", element)


                for content in contents:
                    content_text = content.text
                    if content_text not in content_text_set:
                        content_text_set.add(content_text)
                        print(f"Found content: {content_text}")
                        break

                # Check if new elements were found
                if not elements:
                    print("No more elements found, ending search.")
                    break
                # time.sleep(500)
                # Scroll down to load more content
                if counter == len(elements):
                    # scroll_down(driver)
                    elements = driver.find_elements(By.XPATH, xpath_template)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
