import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set your desired user agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

chrome_options = Options()
#chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-gpu')

# Add user agent to Chrome options
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--disable-logging')

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

driver.get('price tracker website ')
search_locator = (By.ID, 'search')
search_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(search_locator))

# Now you can use 'search_element' for further interactions, such as sending keys
search_element.send_keys('https://www.amazon.in/HP-Anti-Glare-Graphics-15s-eq2213AU/dp/B0BQMZG1SL/ref=sr_1_4?crid=2LINN7TU8O7AI&keywords=laptops+under+%E2%82%B9100000&qid=1704891525&sprefix=%2Caps%2C482&sr=8-4')

# Locate the search button by CLASS_NAME
search_button_locator = (By.ID, 'search-submit')
search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(search_button_locator))

# Click the search button
search_button.click()
time.sleep(4)

# Wait for some time to see the result (you may need to adjust this)
price_row_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'row.p-0')))
present_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ph-pricing-pricing')))
average_price_element = price_row_element.find_element(By.CSS_SELECTOR, '.bg-warning .amount')

# Extract individual price elements
highest_price_element = price_row_element.find_element(By.CSS_SELECTOR, '.bg-danger .amount')
average_price_element = price_row_element.find_element(By.CSS_SELECTOR, '.bg-warning .amount')
lowest_price_element = price_row_element.find_element(By.CSS_SELECTOR, '.bg-info .amount')
prt_price = present_price.text

# Print extracted information
print(f'Highest Price: {highest_price_element.text}')
print(f'Average Price: {average_price_element.text}')
print(f'Lowest Price: {lowest_price_element.text}')
print(f'Present Price is {prt_price}')

# Check if present price is less than average price
if float(prt_price.replace('₹', '').replace(',', '')) < float(average_price_element.text.replace('₹', '').replace(',', '')):
    print('You should buy!')
else:
    print('You should wait.')

# Close the WebDriver session when done
driver.quit()
