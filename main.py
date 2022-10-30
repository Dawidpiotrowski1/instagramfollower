import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = "DawidSanczo1"
userName = "dawid.piotrowski1"
instagramAddress = "https://www.instagram.com"
explorePeopleAddress = "https://www.instagram.com/explore/people/"

cookiesClickSelector = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]"
driver.implicitly_wait(1)
loginInputSelector = '//*[@id="loginForm"]/div/div[1]/div/label/input'
passwordInputSelector = '//*[@id="loginForm"]/div/div[2]/div/label/input'
loginButtonSelector = '//*[@id="loginForm"]/div/div[3]/button/div'
saveInformationNotNowButtonSelector = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button'
afterLoginNotNowButtonSelector = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
proponowaniLudzieOgolnyLink = '//*[@id="mount_0_0_ln"]/div/div/div/div[1]/div/div/div//*[@id="react-root"]/section/main/div/div/div/div/button/div[1]/section/main/div/div[2]'
driver.get(instagramAddress)
cookiesAcceptButton = driver.find_element(By.XPATH, cookiesClickSelector)
cookiesAcceptButton.click()

loginInputField = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,loginInputSelector)))
passwordInputField = driver.find_element(By.XPATH,passwordInputSelector)

loginInputField.send_keys(userName)
passwordInputField.send_keys(password)
loginButton = driver.find_element(By.XPATH,loginButtonSelector)
loginButton.click()

saveInformationNotNowButton = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,saveInformationNotNowButtonSelector)))
saveInformationNotNowButton.click()

afterLoginNotNowButton = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,afterLoginNotNowButtonSelector)))
afterLoginNotNowButton.click()

driver.get(explorePeopleAddress)
driver.implicitly_wait(75)
proponowaniLudzieOgolny = driver.find_element(By.XPATH,proponowaniLudzieOgolnyLink)
for i in len(proponowaniLudzieOgolny):
    print (i.text)



time.sleep(1000)


