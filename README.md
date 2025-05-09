# 6-Digit Code Brute-Forcer (Selenium Tool)

This tool is a Python script that uses Selenium to systematically try all possible 6-digit numerical combinations (from 000000 to 999999) on a web page where a 6-digit code is required. It is designed for security research and authorized testing purposes only.

**Disclaimer:** This tool should only be used on systems where you have explicit permission to conduct such testing. Unauthorized use is unethical and may be illegal. The developers and contributors are not responsible for any misuse of this tool.

## Purpose

This script is intended to automate the process of testing the security of a 6-digit code verification mechanism on a web page. It is specifically designed for scenarios where:

1.  You have manually navigated to the page requiring the 6-digit code.
2.  There is no explicit "Submit" button for the code; the page redirects upon entering the correct code (typically to a home page or a success page).

## Prerequisites

* **Python 3:** Make sure you have Python 3 installed on your system. You can check your version by running `python3 --version` in your terminal.
* **Selenium:** Install the Selenium library using pip:
    ```bash
    pip install selenium
    ```
* **WebDriver:** You need the WebDriver for the browser you intend to use. This script is configured for Google Chrome.
    * **ChromeDriver:** Download the version compatible with your Chrome browser from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
    * Ensure ChromeDriver is either in your system's PATH or its location is specified in the script. (Adding to PATH is recommended).
* **Virtual Environment (Recommended):** It's good practice to use a virtual environment to manage dependencies. See the "Installation" section for instructions.

## Installation

1.  **Clone the repository** (if you've downloaded this code from GitHub):
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```
3.  **Install Selenium within the virtual environment:**
    ```bash
    pip install selenium
    ```
4.  **Set up ChromeDriver:** Follow the instructions in the "Prerequisites" section to download and configure ChromeDriver.

## Setup

1.  **Save the Python script:** Save the provided Python code as a `.py` file (e.g., `code_breaker.py`).
2.  **Configure the script:** Open the `code_breaker.py` file and modify the following variables in the `if __name__ == "__main__":` block:
    * `code_entry_url`: Replace `"YOUR_CODE_ENTRY_PAGE_URL_HERE"` with the actual URL of the web page where you need to enter the 6-digit code.
    * `expected_home_url`: Replace `"YOUR_HOME_PAGE_URL_HERE"` with the URL of the page you expect to be redirected to after successfully entering the correct code.

## Usage

1.  **Activate the virtual environment** (if you created one):
    ```bash
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```
2.  **Navigate to the directory** where you saved the `code_breaker.py` file in your terminal.
3.  **Run the script:**
    ```bash
    python code_breaker.py
    ```
    or
    ```bash
    python3 code_breaker.py
    ```

The script will then launch Chrome, navigate to the specified URL, and begin trying all 6-digit codes. The terminal will display the codes being tried and whether a redirection to the expected home page was detected.

## Important Considerations

* **Ethical Use:** Use this tool responsibly and only on systems you are authorized to test.
* **Rate Limiting:** Be aware that websites may have rate limiting or other security measures to prevent automated attacks. This script does include a small delay (`time.sleep(0.5)`) after each attempt, but you might need to adjust this based on the website's behavior.
* **Success Detection:** The script relies on URL redirection to the `expected_home_url` to determine success. Ensure this is the correct behavior of the target website upon successful code entry. You might need to adjust the success detection logic if the website behaves differently.
* **Error Handling:** This is a basic script and may not include extensive error handling. You might want to add error handling (e.g., `try...except` blocks) to make it more robust.
* **Execution Time:** Trying all 1,000,000 combinations will take a significant amount of time. Be prepared for a potentially long execution.

## Disclaimer

This tool is provided for educational and security research purposes only. The authors are not responsible for any misuse or damage caused by this tool. Use it at your own risk and ensure you have the necessary permissions before testing any website.
