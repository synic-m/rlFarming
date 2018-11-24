from selenium import webdriver as webd
from selenium.webdriver.common.keys import Keys   
from time import sleep

login_password = "pasword"

try:
    ##open driver
    driver = webd.Chrome(r"C:\Users\beata\Downloads\chromedriver_win32/chromedriver.exe")
    driver.get("https://www.itpassportsiken.com/ipkakomon.php")
    
    elem_start_btn = driver.find_element_by_css_selector("#configform > div.img_margin > input") 
    elem_start_btn.click()
    
    number = 1000
    for x in range(number):
        sleep(0.5)

        try:
            elem_ans_txt = driver.find_element_by_css_selector("#answerChar")
            driver.execute_script("arguments[0].style.display = 'block';", elem_ans_txt)
            print(elem_ans_txt.text) 
            if elem_ans_txt.text == 'ア':
               elem_ans_btn = driver.find_element_by_css_selector("#mainCol > div.main.kako.doujou > div.ansbg > ul > li:nth-child(1) > a > button") 
            elif elem_ans_txt.text == 'イ':
               elem_ans_btn = driver.find_element_by_css_selector("#mainCol > div.main.kako.doujou > div.ansbg > ul > li:nth-child(2) > a > button") 
            elif elem_ans_txt.text == 'ウ':
               elem_ans_btn = driver.find_element_by_css_selector("#mainCol > div.main.kako.doujou > div.ansbg > ul > li:nth-child(3) > a > button") 
            elif elem_ans_txt.text == 'エ':
               elem_ans_btn = driver.find_element_by_css_selector("#mainCol > div.main.kako.doujou > div.ansbg > ul > li:nth-child(4) > a > button") 
            else:
                print("error")
        except :
                print("selector ch")
                elem_ans_btn = driver.find_element_by_css_selector("#t > button") 
               
            elem_ans_btn.click()
            print(number)
            sleep(1)
            elem_next_btn = driver.find_element_by_css_selector("#configform > div.bottomBtns > input")
            elem_next_btn.click()
       #driver.close()
    except Exception as e:
        print(e)
        pass


