from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

result = []
stack = ["https://www.techlistic.com/p/demo-selenium-practice.html"]

driver = webdriver.Chrome(options=chrome_options)
while len(stack) > 0 and len(result) < 5:
    driver.get(stack.pop())
    result.append(driver.current_url)
    elements = driver.find_elements_by_tag_name("a")
    for elem in elements:
        url = elem.get_attribute('href')
        if url not in stack:
            stack.append(url)
        elif url not in result:
            stack.append(url)
        elif stack in url:
            stack.append(url)
print(result)
