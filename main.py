"""
MIT License

Copyright (c) 2021 Giovanni Almirante

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



Project Name:           Whatsend
Author:                 Almyyyy
Start Date:             02/26/2021
Description: This program can be used to send a message to a list of phone numbers using WhatsApp Web.



Used Modules:
urllib      used to encode a text of any type in url-encoding (percent-encoding)
time        just for code timing :) ...and Facebook/WhatsApp anti-bot policies
selenium    to embed browser event in Python
            note:       to use this library you need to download the latest chosen browser's webdriver
                        (you can find it here: https://selenium-python.readthedocs.io/installation.html#drivers)
                        and set it as a environment variable (PATH)
                        
                        
                  
How it works:
Basically take a look at this WhatsApp Web Url: https://web.whatsapp.com/send?phone=+391238956456&text=this.+is.+a.+complex.+message%21
Did you notice something? Ok, let me break it down ->       https://web.whatsapp.com/   ->   the basic WhatsApp Web Url              
                                                   ->       send?phone=+391238956456   ->   the recipient phone number argument      
                                                   ->       &text=this.+is.+a.+complex.+message%21   ->   the message encoded in pecent-encoding
If you put that Url in your favourite browser (maybe changing the phone number into an existing one)
it will pop up a classic WhatsApp chat window with the message already written. (note: you must be logged in)                                       
Clear, right? So... Why not generate that Url programmatically?
Now there is one last thing to do, clicks! And here Selenium module comes in.
Briefly. Selenium is able to search for objects in the HTML DOM and emulate events... like clicks! (and other stuff that we will need further on.
With that being said let's jump into the code! :)



Changelog:

- v0.1 project draft with main functions
- v0.1.1 minor bug fix (like internet signal loss or inexitent phone number crashes)
- v0.2 code in now translated from Italian to English because is cool and more people can benefit B) 



{code may still buggy}
"""



import urllib.parse
import time
from selenium import webdriver



def encode_msg():
    print('Codifico il messaggio...')

    f = open('messaggio.txt','r')
    m = f.read()
    f.close()
    
    n = open('encoded.txt','w')
    for x in range(0, len(m), 1024):
        buf = m[x:x+1024]
        z = urllib.parse.quote_plus(buf)
        n.write(z)
    n.close()
    
    return(z)



def gen_link(num, msg):
    link = 'https://web.whatsapp.com/send?phone=' + num + '&text=' + msg
    print("     Genero il link...")
    return link



def open_link():
    browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com/")
    input()

    msg = encode_msg()
    
    with open('numeri.txt') as fp:
        num = fp.readline()
        cnt = 1
        while num:
            try:
                num = num.strip()
                print("Numero {}: {}".format(cnt, num))
                browser.get(gen_link(num, msg))
                #browser.save_screenshot("num.png")
                ctrl = True

                while ctrl:
                    try:     
                        a = browser.find_element_by_class_name('_3SRfO')
                        ctrl = False
                        a = browser.find_element_by_class_name('_1ENRV')
                        ctrl = True
                    except:
                        try:
                            button = browser.find_element_by_class_name('_1E0Oz')
                            button.click()
                            print("     Invio...")

                            while ctrl:
                                try:
                                    a = browser.find_element_by_xpath("//span[@data-testid='msg-time']")
                                except:
                                    print("     Inviato!")
                                    ctrl = False

                            time.sleep(30)
                            ctrl = False
                        except:
                            pass
                        
            
                num = fp.readline()
                cnt += 1
            except:
                pass
                

    browser.close()





def send_msg():
    print("LEGGIMI ATTENTAMENTE!")
    print("Premendo INVIO si aprirà una scheda di WhatsApp Web.")
    print("Scannerizza il codice QR dall'account sul quale vuoi azionare il bot.")
    print("NON CHIUDERE LA SCHEDA MANUALMENTE O LA SESSIONE VERRA' CANCELLATA!")
    print("Appena hai completato l'accesso a WhatsApp Web, torna nuovamente qui e premi INVIO.")

    input()

    open_link()
    print("Invio il messaggio...")



send_msg()
