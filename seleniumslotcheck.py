import base64
import io
import tempfile
import time
from PIL import Image
import cairosvg
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

def get_captcha_code(filepath):
    """Solve captcha using 2Captcha service and return the code."""
    solver = TwoCaptcha('xxxx')
    captcha_id = solver.send(file=filepath, caseSensitive=1)
    time.sleep(10)  # Wait for the captcha to be solved.
    code = solver.get_result(captcha_id)
    return code

def main():
    # Initialize the Chrome driver
    driver = uc.Chrome()
    driver.get("https://consulat.gouv.fr/ambassade-de-france-en-irlande/rendez-vous?name=Visas")
    time.sleep(2)
    
    # Navigate through the website
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div[2]/div[2]/div/button").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div[2]/div[2]/div/ul/li[1]").click()
    time.sleep(1)
    
    # Handle Captcha
    print("Captcha please")
    captcha_image_element = driver.find_element(By.ID, "captcha-image")
    captcha_image_src = captcha_image_element.get_attribute('src')
    base64_data = captcha_image_src.split(",")[1]
    svg_data = base64.b64decode(base64_data)
    png_image = cairosvg.svg2png(bytestring=svg_data)
    
    with tempfile.NamedTemporaryFile(mode='wb+', delete=False) as temp_file:
        temp_file.write(png_image)
        temp_file_name = temp_file.name
    
    captcha_code = get_captcha_code(temp_file_name)
    print(captcha_code)
    
    # Input Captcha Code
    captcha_input_xpath = "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/input"
    driver.find_element(By.XPATH, captcha_input_xpath).send_keys(captcha_code)
    time.sleep(0.5)
    
    # Submit and navigate further based on page response
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/label").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/button").click()
    time.sleep(1)
    
    # Check for availability and respond accordingly
    try:
        elem_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/p").text
        print(elem_text)
        if elem_text == "No appointments are available at the moment but slots will be posted in the coming days.":
            print("No slots available.")
        else:
            print("Appointment slot might be available. Consider notifying via Telegram.")
    except Exception as e:
        print("An error occurred, consider rechecking. Exception:", e)

if __name__ == "__main__":
    main()

