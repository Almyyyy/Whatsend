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
