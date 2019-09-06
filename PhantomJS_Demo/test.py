'''
@author: lgx
@Email:297979949@qq.com
@project: send_mail
@file: test.py
@time: 2019-08-21 17:06
@desc:
'''
from selenium import webdriver
import time
from PIL import Image

url='http://www.weather.com.cn/weather1dn/101280601.shtml'
pjs=webdriver.PhantomJS(executable_path='D:/安装包\phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
pjs.get(url)
pjs.maximize_window()
time.sleep(1)
location=pjs.find_element_by_class_name('weatherBgAll').location
print(location)
size=pjs.find_element_by_class_name('weatherBgAll').size
print(size)
pjs.quit()

coordinate = (int(location['x']) ,int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))

im=Image.open('天气.png')
weather_image=im.crop(coordinate)
weather_image.save("天气情况.png")