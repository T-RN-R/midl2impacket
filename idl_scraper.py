import argparse
import pathlib
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

SCRAPED_DIR = pathlib.Path(__file__).parent / 'scraped'
SCRAPED_DIR.mkdir(exist_ok=True)
DEFAULT_DRIVER = "C:\\Users\\coryc\\Downloads\\chromedriver_win32\\chromedriver.exe"

def process_procotol_link(driver: WebDriver, protocol_name, protocol_link):
    print(f"Processing protocol: {protocol_name}")
    print(f"Navigating to {protocol_link}..")

    driver.get(protocol_link)
    time.sleep(1)
    try:
        idl_link = driver.find_element_by_xpath("//a[contains(text(),'Full IDL')]")
        idl_href = idl_link.get_attribute('href')  
        print(f"Retrieving full IDL for {protocol_name}")
        scraped_protocol = driver.title.rsplit('|', 1)[0].strip()
        driver.get(idl_href)
        time.sleep(1)
        scraped_file_name = f"{protocol_name.lower()[1:-1]}.idl"
        retrieved = datetime.today()
        scraped_idl_data = """\
/*
File: {}
Protocol: {}
Source: {}
Retrieval Date: {}
*/

""".format(scraped_file_name, scraped_protocol, idl_href, retrieved.ctime())
        idl_elements = driver.find_elements_by_xpath("//dl/dd/div/pre")
        for idl_element in idl_elements:
            scraped_idl_data += idl_element.text
            scraped_idl_data += '\n'
        scraped_idl = SCRAPED_DIR / scraped_file_name
        scraped_idl.write_text(scraped_idl_data)
    except NoSuchElementException:
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