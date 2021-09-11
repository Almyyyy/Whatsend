from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib.parse
import time
import csv



stop_threads = False
progress = 0.01

pre = "Ciao sono Roberto di Albalú,\n\n"
pre += "Ti contatto in merito all'ordine che hai effettuato da noi su Amazon:\n\n*"

post = "*\n\nVolevamo sapere se fosse tutto a posto, e se ti piacciono i nostri articoli. Abbiamo a cuore il parere dei nostri clienti.😁\n"




browser = webdriver.Chrome(executable_path=r"webdrivers\chrome\windows\chromedriver.exe")
browser.get("https://web.whatsapp.com/")


def genLink(num, msg):
    link = 'https://web.whatsapp.com/send?phone=' + num + '&text=' + msg
    return link

def encodeMsg(m):
    for x in range(0, len(m), 1024):
        buf = m[x:x+1024]
        e = urllib.parse.quote_plus(buf)
    
    return e

def lastMessage():
    i = 1
    j = 50

    while True:
        msg = "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[" + str(i) + "]"
        try:
            browser.find_element_by_xpath(msg)
            i = i + 1
        except:
            i = i - 2
            break
    
    msg = "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[" + str(i) + "]/div[" + str(j) + "]/div/div"

    try:
        browser.find_element_by_xpath(msg)
        while True:
            msg = "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[" + str(i) + "]/div[" + str(j) + "]/div/div"
            try:
                browser.find_element_by_xpath(msg)
                j = j + 1
            except:
                j = j - 1
                break

    except:
        while True:
            msg = "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[" + str(i) + "]/div[" + str(j) + "]/div/div"
            try:
                browser.find_element_by_xpath(msg)
                break
            except:
                j = j - 1

    return msg      

def delForMe(xpath):
    try:
        div = WebDriverWait(browser, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        hover = ActionChains(browser).move_to_element(div)                                                                              
        hover.perform()

        arrow = browser.find_element_by_class_name('_3e9My')
        arrow.click()

        delbtn = browser.find_element_by_xpath("/html/body/div/div[1]/span[4]/div/ul/div/li[6]/div[1]")
        delbtn.click()

        delforme = browser.find_element_by_xpath("/html/body/div/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[3]/div/div[1]/div")
        delforme.click()
    except:
        print("- error in function delForMe -")

def startCheck():
    while True:
        try:
            browser.find_element_by_class_name('_3J6wB') #generic error banner

            try:
                browser.find_element_by_class_name('_1bpDE') #signal loss banner

            except:
                return False

        except:
            return True

def sendMsg():
    try:
        button = browser.find_element_by_class_name('_4sWnG')
        button.click()

        while True:
            try:
                browser.find_element_by_xpath("//span[@data-testid='msg-time']")
            except:
                return True
    except:
        return False

def mainThread(numberslist, message):
    MAX = 0
    file = open(numberslist, "r")
    for line in file:
        if line != "\n":
            MAX += 1
    file.close()

    msg = encodeMsg(message)
    
    with open(numberslist) as fp:
        num = fp.readline()
        cnt = 1

        while num:
            num = num.strip()
            print("Phone number {}: {}".format(cnt, num))

            try:
                browser.get(genLink(num, msg))
                #browser.save_screenshot("num.png")
                progress = round(100 / MAX * cnt, 2)
                print("Progress: " + str(progress) + "%") 
                while startCheck(num):
                    if sendMsg():
                        print("Sent!")
                        delForMe(lastMessage())
                        browser.get("https://web.whatsapp.com/")
                        
                        start = time.time()
                        while (time.time() - start < 30): # 30 seconds
                            if stop_threads: 
                                #browser.close()
                                return

                        break                 
            
                num = fp.readline()
                cnt += 1

            except:
                pass

def archiveit():
    while True:
        try:
            actions = ActionChains(browser) 
            actions.key_down(Keys.CONTROL)
            actions.key_down(Keys.ALT)
            actions.key_down(Keys.SHIFT)
            actions.send_keys("e")
            actions.key_up(Keys.CONTROL)
            actions.key_up(Keys.ALT)
            actions.key_up(Keys.SHIFT)
            actions.perform()
            break
        except:
            pass

def main():
    input("Premi INVIO dopo il login in WhatsApp Web")

    order_number = "null"

    with open('test.txt', newline = '') as orders:                                                                                          
    	orders_reader = csv.reader(orders, delimiter='\t')
    	for order in orders_reader:

            if order_number != str(order[0]):
                order_number = str(order[0])
                MSG = encodeMsg(pre + str(order[8]) + post)

                phone_number = str(order[6])
                if not phone_number.startswith('+39'):
                    phone_number = "+39" + phone_number

                print("Phone number: " + phone_number)
                print("Order number: " + order_number)

                try:
                    browser.get(genLink(phone_number, MSG))

                    while startCheck():
                        if sendMsg():
                            print("Sent!")
                            #delForMe(lastMessage())

                            archiveit()

                            #browser.get("https://web.whatsapp.com/")
                            
                            start = time.time()

                            while (time.time() - start < 30): # 30 seconds
                                if stop_threads: 
                                    #browser.close()
                                    return

                            break

                except:
                    pass



main()