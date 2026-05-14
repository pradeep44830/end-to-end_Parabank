from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("pradeep@1999")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Pradeep@1999")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    testSuccess = driver.find_element(By.XPATH, "//p[@class='smallText']").text
    print("Login Success...")
    assert "ParaBank" in driver.title
    assert "overview" in driver.current_url
    assert "Welcome" in testSuccess
