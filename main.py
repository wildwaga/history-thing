from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.purposegames.com/game/ap-world-history-regions-map-game')
html = browser.page_source
start_state = 'data-id="meta"'
eas_state = 'data-id="1"'
cas_state = 'data-id="2"'
seas_state = 'data-id="3"'
sas_state = 'data-id="4"'
me_state = 'data-id="5"'
naf_state = 'data-id="6"'
waf_state = 'data-id="7"'
caf_state = 'data-id="8"'
eaf_state = 'data-id="9"'
saf_state = 'data-id="10"'
na_state = 'data-id="11"'
la_state = 'data-id="12"'
c_state = 'data-id="13"'
m_state = 'data-id="14"'
global count
count = 0 
global running
running = True
if (start_state in html):
    browser.execute_script("document.getElementById('start').click()")
time.sleep(0.1)
while running==True:
    html = browser.page_source
    if(eas_state in html):
        browser.execute_script("document.getElementById('1').click()")
        count+=1
    if(cas_state in html):
        browser.execute_script("document.getElementById('2').click()")
        count+=1
    if(seas_state in html):
        browser.execute_script("document.getElementById('3').click()")
        count+=1
    if(sas_state in html):
        browser.execute_script("document.getElementById('4').click()")
        count+=1
    if(me_state in html):
        browser.execute_script("document.getElementById('5').click()")
        count+=1
    if(naf_state in html):
        browser.execute_script("document.getElementById('6').click()")
        count+=1
    if(waf_state in html):
        browser.execute_script("document.getElementById('7').click()")
        count+=1
    if(caf_state in html):
        browser.execute_script("document.getElementById('8').click()")
        count+=1
    if(eaf_state in html):
        browser.execute_script("document.getElementById('9').click()")
        count+=1
    if(saf_state in html):
        browser.execute_script("document.getElementById('10').click()")
        count+=1
    if(na_state in html):
        browser.execute_script("document.getElementById('11').click()")
        count+=1
    if(la_state in html):
        browser.execute_script("document.getElementById('12').click()")
        count+=1
    if(c_state in html):
        browser.execute_script("document.getElementById('13').click()")
        count+=1
    if(m_state in html):
        browser.execute_script("document.getElementById('14').click()")
        count+=1