import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome(executable_path=r"webdrivers\chrome\windows\chromedriver.exe")
browser.get("https://web.whatsapp.com/")



def gen_link(num, msg):
    link = 'https://web.whatsapp.com/send?phone=' + num + '&text=' + msg
    return link

def encode_msg(m):
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
    div = WebDriverWait(browser, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    hover = ActionChains(browser).move_to_element(div)                                                                              
    hover.perform()

    arrow = browser.find_element_by_class_name('QhSbI')
    arrow.click()

    delbtn = browser.find_element_by_xpath("/html/body/div/div[1]/span[4]/div/ul/div/li[5]")
    delbtn.click()

    delforme = browser.find_element_by_xpath("/html/body/div/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[3]/div/div[1]/div")
    delforme.click()

def saveLog(num):
    with open("log.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write("num")

def vai(numberslist, message):

    msg = encode_msg(message)
    
    with open(numberslist) as fp:
        num = fp.readline()
        cnt = 1

        while num:
            num = num.strip()
            print("Phone number {}: {}".format(cnt, num))

            try:
                browser.get(gen_link(num, msg))
                #browser.save_screenshot("num.png")
                ctrl = True

                while ctrl:
                    try:     
                        a = browser.find_element_by_class_name('_3SRfO')
                        ctrl = False
                        a = browser.find_element_by_class_name('_1ENRV')
                        ctrl = True
                        print("Incorrect header! Check log.")
                        saveLog(num)
                    except:
                        try:
                            button = browser.find_element_by_class_name('_1E0Oz')
                            button.click()

                            while ctrl:
                                try:
                                    a = browser.find_element_by_xpath("//span[@data-testid='msg-time']")
                                except:
                                    print("Sent!")
                                    delForMe(lastMessage())
                                    ctrl = False

                            time.sleep(30)
                            ctrl = False
                        except:
                            pass
                        
            
                num = fp.readline()
                cnt += 1

            except:
                pass
                
                
                

    #browser.close()