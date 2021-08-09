import argparse
import pathlib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

SCRAPED_DIR = pathlib.Path(__file__).parent / 'scraped'
SCRAPED_DIR.mkdir(exist_ok=True)
DEFAULT_DRIVER = "<your_chrome_driver_path>"

def process_procotol_link(driver: WebDriver, protocol_name, protocol_link):
    print(f"Processing protocol: {protocol_name}")
    print(f"Navigating to {protocol_link}..")

    driver.get(protocol_link)
    time.sleep(1)
    try:
        idl_link = driver.find_element_by_xpath("//a[contains(text(),'Full IDL')]")
        idl_href = idl_link.get_attribute('href')  
        print(f"Retrieving full IDL for {protocol_name}")
        driver.get(idl_href)
        time.sleep(1)
        idl_element = driver.find_element_by_xpath("//dl/dd/div/pre")
        scraped_idl = SCRAPED_DIR / f"{protocol_name.lower()[1:-1]}.idl"
        scraped_idl.write_text(idl_element.text)
    except NoSuchElementException as nse:
        print(f"No link for Full IDL in {protocol_name}/{protocol_link}")

def scrape(webdriver_path: pathlib.Path):
    driver = webdriver.Chrome(webdriver_path)
    driver.get("https://docs.microsoft.com/en-us/openspecs/windows_protocols/MS-WINPROTLP/92b33e19-6fff-496b-86c3-d168206f9845")
    assert "MS-WINPROTLP" in driver.title
    docs = driver.find_element_by_xpath("//span[text()='Technical Documents']")
    expander = docs.find_element_by_xpath("..")
    expander.send_keys(Keys.RETURN)
    links = expander.find_elements_by_xpath('ul/li/a')
    protocol_data = []
    for link in links[1:]:
        href = link.get_attribute('href')
        protocol_name = link.text[:link.text.find(']')+1]
        protocol_data.append((protocol_name, href))
    for protocol_info in protocol_data:
        process_procotol_link(driver, protocol_info[0], protocol_info[1])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome", required=False, help="Chrome WebDriver location", default=DEFAULT_DRIVER)
    args = parser.parse_args()
    webdriver_path = pathlib.Path(args.chrome)
    if not webdriver_path.exists():
        print(f"WebDriver path {args.chrome} does not exist!")
        return -1
    scrape(webdriver_path)

if __name__ == '__main__':
    main()