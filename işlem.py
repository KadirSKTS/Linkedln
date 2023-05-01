from selenium import webdriver
import time
import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("BU KOD SELENİUM İLE YAZILMIŞ VE LİNKEDLİN HESABINIZA GİREREK BENİM HESABIMI GÖREBİLECEĞİNİZ BASİT BİR BOT")
mail = input("linkedln mail adresinizi giriniz: ")
pasword = input("linkedlin şifrenizi giriniz: ")

driver = webdriver.Chrome()   # crome açmak için kullandık

driver.get("https://tr.linkedin.com/") #

driver.maximize_window()  # tarayıcıyı tam ekran haline getirir

time.sleep(3)  # kodun çalışmasını birsüre bekletir


e_mail_input = driver.find_element(by = By.XPATH, value='//*[@id="session_key"]')

e_mail_input.send_keys(mail)

time.sleep(3)

pasword_input = driver.find_element(by = By.XPATH, value='//*[@id="session_password"]')

pasword_input.send_keys(pasword +Keys.ENTER )

time.sleep(3)

search = driver.find_element(by = By.XPATH, value='//*[@id="global-nav-typeahead"]/input') # arama çubuğu
search.click()
time.sleep(3)
search.send_keys('Abdulkadir Işıktaş'+ Keys.ENTER)

time.sleep(3)

meet = driver.find_element(by= By.XPATH, value="/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/ul/li/div/a/div/div/div[1]/div/div/span[1]/span/a/span/span[1]")
meet.click()

time.sleep(60)

driver.quit() # sayfayı kapattık

