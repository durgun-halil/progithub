from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
url="https://www.hepsiemlak.com/istanbul/konut"
driver.get(url)
time.sleep(13)
tikla=driver.find_element('xpath',"//*[@id='modal-3b391045-3564-4bb1-8543-a5b366e7864b']/div/div/header/button") 
tikla.click()
time.sleep(10)
ev1=driver.find_element('xpath',"//*[@id='37108-4020']/div/div[2]/div[1]/a") 
ev1.click()
time.sleep(10)
bilgiler=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler)
print("")
driver.back()
time.sleep(10)

with open("bilgiler.txt", "w") as dosya:
    dosya.write(bilgiler)  # Veriyi dosyaya yazar

driver.execute_script("window.scrollTo(30, document.body.scrollHeight);")
ev2=driver.find_element('xpath',"//*[@id='125107-153']/div/div[2]/div[1]/a") 
ev2.click()
time.sleep(5)
bilgiler1=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler1)
print("")
driver.back()
time.sleep(5)

with open("bilgiler1.txt", "w") as dosya:
    dosya.write(bilgiler1) 

driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev3=driver.find_element('xpath',"//*[@id='125107-809']/div/div[2]/div[1]/a") 
ev3.click()
time.sleep(5)
bilgiler2=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler2)
print("")
driver.back()
time.sleep(5)

with open("bilgiler2.txt", "w") as dosya:
    dosya.write(bilgiler2) 


driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev4=driver.find_element('xpath',"//*[@id='135302-98']/div/div[2]/div[1]/a") 
ev4.click()
time.sleep(5)
bilgiler3=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler3)
print("")
driver.back()
time.sleep(5)

with open("bilgiler3.txt", "w") as dosya:
    dosya.write(bilgiler3) 


driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev5=driver.find_element('xpath',"//*[@id='38942-1922']/div/div[2]/div[1]/a") 
ev5.click()
time.sleep(5)
bilgiler4=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler4)
print("")
driver.back()
time.sleep(5)

with open("bilgiler4.txt", "w") as dosya:
    dosya.write(bilgiler4) 

driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev6=driver.find_element('xpath',"//*[@id='38942-1923']/div/div[2]/div[1]/a") 
ev6.click()
time.sleep(5)
bilgiler5=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler5)
print("")
driver.back()
time.sleep(5)


with open("bilgiler5.txt", "w") as dosya:
    dosya.write(bilgiler5) 

driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev7=driver.find_element('xpath',"//*[@id='38942-1924']/div/div[2]/div[1]/a") 
ev7.click()
time.sleep(5)
bilgiler6=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler6)
print("")
driver.back()
time.sleep(5)

with open("bilgiler6.txt", "w") as dosya:
    dosya.write(bilgiler6)  



driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev8=driver.find_element('xpath',"//*[@id='38942-1926']/div/div[2]/div[1]/a") 
ev8.click()
time.sleep(5)
bilgiler7=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler7)
print("")
driver.back()
time.sleep(5)


with open("bilgiler7.txt", "w") as dosya:
    dosya.write(bilgiler7)  

driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev9=driver.find_element('xpath',"//*[@id='38942-1929']/div/div[2]/div[1]/a") 
ev9.click()
time.sleep(5)
bilgiler8=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler8)
print("")
driver.back()
time.sleep(5)

with open("bilgiler8.txt", "w") as dosya:
    dosya.write(bilgiler8)  


driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")
ev10=driver.find_element('xpath',"//*[@id='38942-1930']/div/div[2]/div[1]/a") 
ev10.click()
time.sleep(5)
bilgiler9=driver.find_element('xpath',"//*[@id='__layout']/div/div/section[3]/div/div[1]/div[1]/section[1]/div[4]/div").text
print(bilgiler9)
print("")
driver.back()
time.sleep(5)

with open("bilgiler9.txt", "w") as dosya:
    dosya.write(bilgiler9)  

driver.close()
