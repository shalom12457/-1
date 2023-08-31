from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

selectors = {
    'username': 'user-name',
    'passowrd': 'password'
}


def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def login(driver, credentials, username="standard_user"):
    username_field = driver.find_element(By.ID, selectors["username"])
    password_field = driver.find_element(By.ID, selectors["password"])
    login_button = driver.find_element(By.NAME, "login-button")

    username_field.send_keys(username)
    password_field.send_keys("secret_sauce")
    login_button.click()

    # wait for page to load
    driver.implicitly_wait(1000)

    # Add assertion to validate successful login
    return driver.current_url


def test_sorting(driver, credentials):
    sort_button = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_button.click()
    sort_button.send_keys(Keys.DOWN)
    sort_button.send_keys(Keys.DOWN)
    sort_button.send_keys(Keys.ENTER)
    # get the list of items
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    # convert the list of items to a list of prices
    prices = [float(item.text[1:]) for item in items]

    return prices == sorted(prices)


def test_images_match(driver):
    problem_images = get_inventory_images(driver)

    logout(driver)

    login(driver, "problem_user")

    regular_images = get_inventory_images(driver)

    return [image for image in problem_images if image not in regular_images]


def get_inventory_images(driver):
    return [image.src for image in driver.find_elements(By.CLASS_NAME, "inventory_item_img")]


def logout(driver):
    hamburger_button = driver.find_element(By.ID, "react-burger-menu-btn")
    hamburger_button.click()
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
