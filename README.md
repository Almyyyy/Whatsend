# Whatsend

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

#

### Description
A python bot that uses WhatsApp Web to send a message to a list of phone numbers

Project Name | Author | Start Date
-|-|-
Whatsend | Almyyyy | 02/26/2021

#

### Used Modules

Module Name | Description
-|-
urllib | used to encode a text of any type in url-encoding (percent-encoding)
time | just for code timing :) ...and Facebook/WhatsApp anti-bot policies
selenium | to embed browser event in Python

Note: to use the selenium library you need to download the latest chosen browser's webdriver (you can find it [here](https://selenium-python.readthedocs.io/installation.html#drivers)) and set it as a environment variable (PATH)

#

### How it works
Basically take a look at this WhatsApp Web Url:
###
https://web.whatsapp.com/send?phone=+391238956456&text=this.+is.+a.+complex.+message%21
###
Did you notice something? Ok, let me break it down 

Code | Description
-|-
https://web.whatsapp.com/ | the basic WhatsApp Web Url
send?phone=+391238956456 | the recipient phone number argument
&text=this.+is.+a.+complex.+message%21 | the message encoded in pecent-encoding


If you put that Url in your favourite browser (maybe changing the phone number into an existing one) it will pop up a classic WhatsApp chat window with the message already written. Note: you must be logged in.
###
Clear, right? So... Why not generate that Url programmatically?
###
Now there is one last thing to do, clicks! And here Selenium module comes in.
###
Briefly. Selenium is able to search for objects in the HTML DOM and emulate events... like clicks! (and other stuff that we will need further on.
###
With that being said let's jump into the code! :man_technologist:

#

### Changelog:

- [x] v0.1 project draft with main functions
- [x] v0.1.1 minor bug fix (like internet signal loss or inexitent phone number crashes)
- [x] v0.2 code is now translated from Italian to English because is cool and more people can benefit :sunglasses:
- [x] v0.3 now the program has a GUI, the code is better written and has been introduced a function that eliminates the message "for me" once sent
- [ ] introduce threading, improve the gui and error handling


### {code may still buggy} :purple_heart:
