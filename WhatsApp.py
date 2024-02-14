# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback  # Import traceback for detailed error information

# Config
login_time = 30                 # Time for login (in seconds)
new_msg_time = 5                # Time for a new message (in seconds)
send_msg_time = 5               # Time for sending a message (in seconds)
country_code = 1                # Set your country code
action_time = 2                 # Set time for button click action
image_path = 'image.png'        # Absolute path to your image

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = file.read()

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)

        try:
            # Wait for the attachment button to be clickable
            attach_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '._1OT67')))
            attach_btn.click()
            time.sleep(action_time)

            # Find and send image path to input
            msg_input = driver.find_elements(By.CSS_SELECTOR, '._2UNQo input')[1]
            msg_input.send_keys(image_path)
            time.sleep(action_time)
        except Exception as e:
            print(f"Error while handling attachment: {e}")
            print("Stacktrace:")
            traceback.print_exc()
            continue  # Skip to the next iteration if there is an issue with the attachment

        # Start the action chain to write the message
        actions = ActionChains(driver)
        try:
            msg_input = driver.find_element(By.CSS_SELECTOR, '._2A8P4')
            msg_input.click()
            for line in msg.split('\n'):
                actions.send_keys(line)
                # SHIFT + ENTER to create the next line
                actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(send_msg_time)
        except Exception as e:
            print(f"Error while handling message sending: {e}")
            print("Stacktrace:")
            traceback.print_exc()

# Quit the driver
driver.quit()
