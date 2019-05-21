import time

from selenium import webdriver

wd = webdriver.Chrome('D:\PythonStudy\새 폴더\chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(5)



html = wd.page_source
print(html)
wd.quit()