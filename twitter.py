from tkinter import *
import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from PIL import ImageTk, Image
import pandas as pd
import os
def google_search():
 search_term = search_box.get()
 kullanici_adi1=admin.get()
 yaz=ald.get()
 driver = webdriver.Chrome()
 driver=webdriver.Chrome()
 url="https://twitter.com/"
 driver.get(url)
 time.sleep(10)
 kapat=driver.find_element('xpath','//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
 kapat.click() 
 time.sleep(15)
 kullanici_adi=driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
 kullanici_adi.click()
 kullanici_adi.send_keys(kullanici_adi1)
 
 ileri=driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
 time.sleep(10)
 alver=driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
 alver.click()
 alver.send_keys(yaz)
 

 
 giris=driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
 time.sleep(20)
 search_bar=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
 search_bar.click()
 #ara.send_keys("#besiktas")
 search_bar.send_keys(search_term)
 search_bar.send_keys(Keys.ENTER)
 time.sleep(10)
 last_=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[4]/a/div/div/span')
 last_.click()
 time.sleep(10)

 al=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/article/div/div')
 al.click()
 time.sleep(3)
 yorum=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div').text
 print(yorum)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 al1=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]')
 al1.click()
 time.sleep(5)
 yorum1=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum1)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")

 time.sleep(6)


 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN)
 time.sleep(5)
 

 al2=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div')
 al2.click()
 time.sleep(5)
 yorum2=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum2)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN)
 time.sleep(3)


 al3=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div/div[2]')
 al3.click()
 time.sleep(5)
 yorum3=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum3)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN)    
 time.sleep(3)


 al4=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]')
 al4.click()
 time.sleep(5)
 yorum4=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum4)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN)
 time.sleep(3)


 al5=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]')
 al5.click()
 time.sleep(5)
 yorum5=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum5)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN) 
 time.sleep(3)


 al6=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]')
 al6.click()
 time.sleep(5)
 yorum6=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum6)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)")
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN) 

 time.sleep(3)


 al7=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[5]/div/div/article/div/div/div[2]')
 al7.click()
 time.sleep(5)
 yorum7=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum7)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)") 
 time.sleep(5)

 body = driver.find_element(By.TAG_NAME, 'body')
 body.send_keys(Keys.PAGE_DOWN) 

 time.sleep(3)

 al8=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]')
 al8.click()
 time.sleep(5)
 yorum8=driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div').text
 print(yorum8)
 time.sleep(5)
 driver.execute_script("window.history.go(-1)") 
 time.sleep(5)

 dosya = open("metin.txt","a",encoding="utf-8")
 dosya.write(yorum1)
 dosya.write(yorum)
 dosya.write(yorum3)
 dosya.write(yorum4)
 dosya.write(yorum5)
 dosya.write(yorum6)
 dosya.write(yorum7)
 dosya.write(yorum8)

 dosya=open("metin1.txt","a",encoding="utf-8")
 dosya.write(yorum)
 dosya.write(yorum1)
 dosya.write(yorum2)
 dosya.write(yorum3)
 dosya.write(yorum4)
 dosya.write(yorum5)
 dosya.write(yorum6)
 dosya.write(yorum7)
 dosya.write(yorum8)
 

 driver.close()
 dosya = open("metin1.txt","a",encoding="utf-8")
 dosya.write(yorum1)
 dosya.write(yorum)
 dosya.write(yorum3)
 dosya.write(yorum4)
 dosya.write(yorum5)
 dosya.write(yorum6)
 dosya.write(yorum7)
 dosya.write(yorum8)




root = Tk()
root.geometry("300x300")
root.title("twitter")

search_box = Entry(root, width=30)
search_box.place(x=58,y=100)

admin=Entry(root,width=20)
admin.place(x=88,y=50)

ald=Entry(root,width=20)
ald.place(x=88,y=75)


admin_yazi=Label(root,text="Admin")
admin_yazi.place(x=40,y=48)

password_yazi=Label(root,text='Password')
password_yazi.place(x=30,y=71)

konu_yazi=Label(root,text='Konu')
konu_yazi.place(x=21,y=98)

root.resizable(False,False)

search_button = Button(root, text="Search", command=google_search)
search_button.place(x=130,y=130)
root.configure(bg="light blue")





root.mainloop()


search_button = Button(root, text="Search", command=google_search)
search_button.place(x=10,y=10)

ara=Button(root,text="Ara",command=google_search)
ara.pack()




