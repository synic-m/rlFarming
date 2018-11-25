from selenium import webdriver as webd
from time import sleep

print("login")
twi_id = "@_zith"#input()
twi_pass = "398267qg"#input() 
tweets = int(input())

##open driver
driver = webd.Chrome("C:/Users/beata/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.twitter.com/login")

elem_login_id_form = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
elem_login_id_form.send_keys(twi_id)

elem_login_pass_form = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
elem_login_pass_form.send_keys(twi_pass)

elem_login_btn = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > div.clearfix > button")
elem_login_btn.click()

#toprofile

elem_goto_profile = driver.find_element_by_css_selector("#page-container > div.dashboard.dashboard-left > div.DashboardProfileCard.module > div > div.ProfileCardStats > ul > li:nth-child(1) > a > span.ProfileCardStats-statLabel.u-block")
elem_goto_profile.click()
sleep(0.5)

for x in range(tweets):
    try:
        elem_tweet = driver.find_element_by_class_name("ProfileTweet-actionButton")
        elem_tweet.click()
        sleep(0.5)
        elem_twi_del_btn = driver.find_element_by_class_name("Delete Tweet")#ここ要素つらい
        elem_twi_del_btn.click()
        sleep(0.5)
        elem_del_btn = driver.find_element_by_css_selector("#delete-tweet-dialog-dialog > div.modal-content > div.modal-footer > button.EdgeButton.EdgeButton--danger.delete-action")
        elem_del_btn.click()
    except Exception as e:
        print(e)
#        elem_rt_btn = driver.find_element_by_css_selector("#permalink-overlay-body > div > div.permalink.light-inline-actions.stream-uncapped.has-replies.original-permalink-page > div.permalink-inner.permalink-tweet-container > div > div.stream-item-footer > div.ProfileTweet-actionList.js-actions > div.ProfileTweet-action.ProfileTweet-action--retweet.js-toggleState.js-toggleRt > button.ProfileTweet-actionButtonUndo.js-actionButton.js-actionRetweet")
#        elem_rt_btn.click()
#

