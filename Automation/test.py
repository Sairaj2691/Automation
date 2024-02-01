from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,TimeoutException
import time

url = 'http://practice.automationtesting.in/'
username='Tree@test.com'
password='Tree@Test1234'
adblock=r'CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_55_0_0.crx'
# adblock=r'C:\Users\anonymus\Documents\SAI_Assignment\adblock.crx'
def init_driver():    
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_extension(adblock)
    driver = webdriver.Chrome(options=options)
    return driver


def enter_url():
    driver=init_driver()
    wait=WebDriverWait(driver,10)
    driver.get(url)
    try: 
        #<li id="menu-item-50" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://practice.automationtesting.in/my-account/">My Account</a> </li>
        # MyAccount = driver.find_element(By.ID,'menu-item-121212')
        time.sleep(5)
        MyAccount = wait.until(EC.presence_of_element_located((By.ID,'menu-item-50')))
        MyAccount.click()
        #login
        # <input type="text" class="woocommerce-Input woocommerce-Input--text input-text" name="username" id="username" value="">
        reg_email = wait.until(EC.presence_of_element_located((By.ID,'username')))
        reg_email.send_keys(username)
        # <input class="woocommerce-Input woocommerce-Input--text input-text" type="password" name="password" id="password">
        reg_password = wait.until(EC.presence_of_element_located((By.ID,'password')))
        reg_password.send_keys(password)
        # <input type="submit" class="woocommerce-Button button" name="login" value="Login">
        login = wait.until(EC.presence_of_element_located((By.NAME,'login')))
        login.click()
        #click myAcccount
        # <a href="https://practice.automationtesting.in/my-account/">My Account</a>
        # <li id="menu-item-50" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-36 current_page_item"><a href="https://practice.automationtesting.in/my-account/">My Account</a> </li>
        # /html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a
        myAccount=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')))
        myAccount.click()
        # Click account details
        # /html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[5]/a
        accountDetails=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[5]/a')))
        accountDetails.click()
        time.sleep(100000)
        #user can enter details



    except (ElementNotVisibleException,NoSuchElementException,TimeoutException):
        print('error')


if __name__=='__main__':
    enter_url()