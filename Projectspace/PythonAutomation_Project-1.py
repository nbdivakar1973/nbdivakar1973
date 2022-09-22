import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import ActionChains


def browse(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com")
        action = ActionChains(driver)
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(by=By.XPATH, value ='//input[@placeholder="Username" and @name="username"]').send_keys("Admin")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//input[@placeholder="Password" and @name="password"]').send_keys("admin123")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()

       # Create new employee
        driver.find_element(by=By.LINK_TEXT, value="Add Employee").click()

        time.sleep(3)

        driver.find_element(by=By.XPATH, value='//input[@name="firstName" and @placeholder="First Name"]').send_keys("Zakeer")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//input[@name="lastName" and @placeholder="Last Name"]').send_keys("Hussain")
        time.sleep(3)

        driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()
        time.sleep(10)

        #click on Admin panel
        driver.find_element(by=By.XPATH, value='//span[text()="Admin"]').click()
        time.sleep(4)
        # click on Add button
        driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(3)

        #input employee name
        driver.find_element(by=By.XPATH, value='//input[@placeholder="Type for hints..."]').send_keys("Zakeer")
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span').click()
        time.sleep(3)
        # input status as enabled
        driver.find_element(By.XPATH, value='//form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
        driver.find_element(By.XPATH,'//form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]').click()

        # input Role as ESS
        time.sleep(3)
        driver.find_element(By.XPATH, '//form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click()
        driver.find_element(By.XPATH, '//form/div[1]/div/div[1]/div/div[2]/div/div/div[3]').click()

        #input username
        driver.find_element(by=By.XPATH, value='//form/div[1]/div/div[4]/div/div[2]/input').send_keys("Zakeer1234")
        time.sleep(3)

        #input password and confirm password
        driver.find_element(by=By.XPATH, value='//form/div[2]/div/div[1]/div/div[2]/input').send_keys("Zakeer@1984")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//form/div[2]/div/div[2]/div/div[2]/input').send_keys("Zakeer@1984")
        time.sleep(3)

        #save the users in admin panel
        driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()
        time.sleep(10)

        # search for user in Admin panel
        driver.find_element(By.XPATH, '//form/div[1]/div/div[1]/div/div[2]/input').send_keys("Zakeer1234")
        time.sleep(3)

        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

        #Log out
        driver.find_element(By.XPATH, value='//p[@class="oxd-userdropdown-name"]').click()
        driver.find_element(By.XPATH, value='//a[@href="/web/index.php/auth/logout" and text()="Logout"]').click()
        time.sleep(5)
        driver.close()
        time.sleep(5)
        # Restarting driver
        driver = webdriver.Firefox(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(6)
        # Relogin:
        driver.find_element(by=By.XPATH, value='//input[@placeholder="Username" and @name="username"]').send_keys(
            "Admin")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//input[@placeholder="Password" and @name="password"]').send_keys(
            "admin123")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()






browse('firefox')



