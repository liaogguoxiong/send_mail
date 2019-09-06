'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: 获取天气截图_无界面.py
@time: 2019-08-20 15:01
@desc:
'''

from selenium import webdriver
from PIL import Image

url='http://www.weather.com.cn/weather1dn/101250101.shtml'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
driver.maximize_window()
print(driver.get_window_size())
driver.save_screenshot('天气.png')
location=driver.find_element_by_class_name('weatherBgAll').location
print(location)
size=driver.find_element_by_class_name('weatherBgAll').size
print(size)
driver.quit()

coordinate = (int(location['x']) ,int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))

im=Image.open('天气.png')
weather_image=im.crop(coordinate)
weather_image.save("天气情况.png")
