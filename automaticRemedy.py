# -*- coding: GBK -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

import sys
import getopt

def isElementExist(element):  # �жϺ���
    flag = True
    try:
        browser.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag

opts, args = getopt.getopt(sys.argv[1:], "hu:p:d:")
username = ""
password = ""
driverpath = ""

for op, value in opts:
    if op == "-u":
        username = value
    elif op == "-p":
        password = value
    elif op == "-d":
        driverpath = value
    elif op == "-h":
        print "-u ...  username"
        print "-p ...  password"
        print "-d ...  driver path"
        print ""
        print "Please download the chrome driver before use"
        print "driver download and version, CSDN link ��http://blog.csdn.net/chaomaster/article/details/52963265"
        print "when the script exit ,we must log out the remedy"
        print "Please ensure that the parameters of the input is correct, otherwise may cause driver abnormal or logon failure"
        sys.exit()

if len(sys.argv) < 4:
    print "please input parameters ... use '-h' to see help "
    sys.exit()


# �������ü����� CSDN ���� ��http://blog.csdn.net/chaomaster/article/details/52963265

# browser = webdriver.Firefox(executable_path='/Users/xuechao/seleniumSupport/geckodriver')
browser = webdriver.Chrome(executable_path=driverpath)

browser.get('https://chinabluemix.itsm.unisysedge.cn/arsys/shared/loggedout.jsp')
browser.implicitly_wait(30)


# ��¼ remedy
browser.find_element_by_id('username-id').send_keys(username)
browser.find_element_by_id('pwd-id').send_keys(password)
browser.find_element_by_id('loginText').click()


# ��������
locator1 = (By.XPATH, ".//*[@id='WIN_1_304017100']/div/div")  # ��λ��ָ��ҳ�水ť
locator2 = (By.CSS_SELECTOR, ".BaseTableCellOdd.BaseTableCellOddColor.BaseTableStaticText")  # ��λ ticket

# �����ѭ��

i = 1  # ����

enTestString = "test"
cnTestString = u"����"

while True :
    try:
        WebDriverWait(browser, 30, 0.5).until(EC.visibility_of_element_located(locator1))
        browser.find_element_by_xpath(".//*[@id='WIN_1_304017100']/div/div").click()

    finally:
        try:
            WebDriverWait(browser, 30000000, 0.5).until(EC.visibility_of_element_located(locator2))  # ģ��ȴ� ʱ�����޴�

            testString = browser.find_element_by_xpath(".//*[@id='T302087200']/tbody/tr[2]/td[2]/nobr/span").text
            if ((enTestString in testString) == False) and ((cnTestString in testString) == False):
                doubleClickArea = browser.find_element_by_css_selector(
                ".BaseTableCellOdd.BaseTableCellOddColor.BaseTableStaticText")
                ActionChains(browser).double_click(doubleClickArea).perform()

        finally:
            try:
                browser.find_element_by_xpath(".//*[@id='arid_WIN_2_536870940']").send_keys("in progress")  # ��ӳ�ʼ��Ӧ

                browser.find_element_by_xpath(".//*[@id='WIN_2_536870924']/div/div").click()  # ����
                print "already deal " + str(i) + " ticket"
                i += 1
                time.sleep(2)
                browser.refresh()  # �����ˢ��
            except:
                browser.refresh()





# locator2 = (By.XPATH, ".//*[@id='T302087200']/tbody/tr[2]/td[@class='BaseTableCellOdd BaseTableCellOddColor BaseTableStaticText'][1]")
# try:
#     WebDriverWait(browser, 30, 0.5).until(EC.visibility_of_element_located(locator2))
#     doubleClickArea = browser.find_element_by_xpath(".//*[@id='T302087200']/tbody/tr[2]/td[@class='BaseTableCellOdd BaseTableCellOddColor BaseTableStaticText'][1]")
#     ActionChains(browser).double_click(doubleClickArea).perform()
#     print '��ȡ�ɹ�'
# finally:
#     browser.close()


# ע�� remedy
# print '��ʼע��'
# browser.find_element_by_xpath('.//*[@id="WIN_0_300000044"]/div/div').click()
#
#
# browser.implicitly_wait(30)
#
# browser.quit()

