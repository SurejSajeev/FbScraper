from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":

    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')

    driver = webdriver.Safari()
    driver.get('https://www.facebook.com/')
    driver.find_element(By.ID, 'email').send_keys('surejsajeev@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Myfb@92')
    driver.find_element(By.NAME, 'login').click()
    import time
    time.sleep(5)  # Wait for the page to load
    driver.get('https://www.facebook.com/groups/117412174975402')

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)

    # Example XPath: Looks for anchor tags within posts that contain user profile links
    post_authors = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@id, ":r")]/span/span/a/strong/span')))

    for author in post_authors:
        print(author.text)

