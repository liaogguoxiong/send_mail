'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: get_weather_info.py
@time: 2019-08-19 21:07
@desc:
'''

from  selenium import webdriver
import time
from PIL import Image

url='http://www.weather.com.cn/weather1dn/101280601.shtml'
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.execute_script("document.body.style.zoom='0.75'")
time.sleep(5)
driver.save_screenshot('天气.png')
location=driver.find_element_by_class_name('weatherBgAll').location
print(location)
size=driver.find_element_by_class_name('weatherBgAll').size
print(size)
driver.quit()

coordinate = (int(location['x'])*0.75 ,int(location['y'])*0.75, int(location['x'] + size['width'])*0.75,
              int(location['y'] + size['height'])*0.75)

im=Image.open('天气.png')
weather_image=im.crop(coordinate)
weather_image.save("天气情况.png")



