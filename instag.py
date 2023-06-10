from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import ImageTk, Image
from PIL import ImageTk, Image
import os

import pandas as pd
def google_search():
    search_term = search_box.get()
    kullanici_adi1=admin.get()
    #sifre=sifremiz.get()
    yaz=al.get()
    driver = webdriver.Chrome()
    driver=webdriver.Chrome()
    url="https://z-p15.www.instagram.com/?hl=tr"
    driver.get(url)
    time.sleep(10)

    kullanici_adi=driver.find_element('xpath','//*[@id="loginForm"]/div/div[1]/div/label/input')
    kullanici_adi.click()
    kullanici_adi.send_keys(kullanici_adi1)
    
    
    
    
    time.sleep(2)
    
    

    alver=driver.find_element('xpath','//*[@id="loginForm"]/div/div[2]/div/label/input')
    alver.click()
    alver.send_keys(yaz)

    git=driver.find_element('xpath','//*[@id="loginForm"]/div/div[3]/button/div')
    git.click()

    
    
    
    
    time.sleep(20)
    tik1=driver.find_element('xpath','//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]')
    tik1.click()
    tik2=driver.find_element('xpath','//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    tik2.click()

    search_bar = driver.find_element('xpath', "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")  
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)
    
    #search_bar.submit()
    time.sleep(5)
    ara=driver.find_element('xpath','//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
    time.sleep(10)

    post1=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]')
    post1.click()
    time.sleep(10)
    yorum1=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum1)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)

    post2=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    post2.click()
    time.sleep(10)
    yorum=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)

    post3=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div')
    post3.click()
    time.sleep(10)
    yorum3=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum3)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)

    post4=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div')
    post4.click()
    time.sleep(10)
    yorum4=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum4)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)

    post5=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[2]/a/div')
    post5.click()
    time.sleep(10)
    yorum5=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum5)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)

    post6=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div')
    post6.click()
    time.sleep(10)
    yorum6=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum6)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 50);")

    post7=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[1]/a/div')
    post7.click()
    time.sleep(10)
    yorum7=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum7)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)


    post8=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[2]/a/div')
    post8.click()
    time.sleep(10)
    yorum8=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum8)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)


    post9=driver.find_element('xpath','//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a/div')
    post9.click()
    time.sleep(10)
    yorum9=driver.find_element('xpath','/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]').text
    print(yorum9)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)


    


    dosya = open("metin.txt","a",encoding="utf-8")
    dosya.write(yorum1)
    dosya.write(yorum)
    dosya.write(yorum3)
    dosya.write(yorum4)
    dosya.write(yorum5)
    dosya.write(yorum6)
    dosya.write(yorum7)
    dosya.write(yorum8)
    dosya.write(yorum9)

    
    
    driver.close()



root = Tk()
root.geometry("300x300")
root.title("İnstegram")

search_box = Entry(root, width=30)
search_box.place(x=58,y=100)

admin=Entry(root,width=20)
admin.place(x=88,y=50)

al=Entry(root,width=20)
al.place(x=88,y=75)


"""
try:
    
    img = Image.open("icon.png")
    img = img.resize((150, 150), Image.ANTIALIAS)

    
    photoImg = ImageTk.PhotoImage(img)


    label = Label(root, image=photoImg)
    label.pack()

except FileNotFoundError as e:
    print(f"Hata: {e}")
except Exception as e:
    print(f"Hata: {e}")
"""
search_button = Button(root, text="Search", command=google_search)
search_button.place(x=130,y=130)
root.configure(bg="pink")

admin_yazi=Label(root,text="Admin")
admin_yazi.place(x=40,y=48)

password_yazi=Label(root,text='Password')
password_yazi.place(x=30,y=71)

konu_yazi=Label(root,text='Konu')
konu_yazi.place(x=21,y=98)

root.resizable(False,False)

root.mainloop()
