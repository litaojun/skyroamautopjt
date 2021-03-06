#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
from skyroamautopjt.util.readExecl import operExcel
reload(sys)
sys.setdefaultencoding('utf8')
def test():
    pass


#selenium2.0关于python的常用函数（一）
#(2013-05-15 15:42:36)
#转载▼
#	分类： selenium
#
#新建实例driver = webdriver.Chrome() 
#
#1.通过标签属性Id查找元素
#
#方法：find_element_by_id(element_id)
#
#实例：driver.find_element_by_id("iptUsername")
#
#2.通过标签属性name查找元素
#
#方法：find_element_by_name(element_name)
#
#实例：driver.find_element_by_id("inputPwname")
#
#3.通过标签Xpath路径查找元素
#
#方法：find_element_by_xpath(xpath)
#
#实例：driver.find_element_by_xpath("//div[@id='menuContainer']/div/div/ul/li[4]/a")
#
#4.通过标签名tagname查找元素
#
#方法：find_element_by_tag_name(tag_name)
#
#实例：driver.find_element_by_tag_name("input")
#
#注意：通过tag_name查找时使用find_element_by_tag_name查找到的是第一个标签的tag_name
#
#5.通过标签中的元素文本链接查找元素
#
#方法：find_element_by_link_text(link_text)
#
#实例：driver.find_element_by_link_text('登  录')
#
#6.通过标签的class属性查找元素
#
#方法：find_elements_by_class_name(class_name)
#
#实例：driver.find_elements_by_class_name("x-panel-body")
#
#7.通过css样式查找元素
#
#方法：find_element_by_css_selector()
#
#实例：driver.find_element_by_css_selector("input.btn")
#温馨提示：find_elements_by_id()查询到的是一个集合，如果id名字重复的时候可以采取find_elements_by_id()，其他的查询方式同理；
#
#8.浏览器中加载url
#
#方法：get(url)
#
#实例：driver.get("http//:www.baidu.com")
#
#9.向前
#
#方法：forward()
#
#实例：driver.forward()
#
#10.返回当前会话中的cookies
#
#方法：get_cookies()
#
#实例：driver.get_cookies()
#
#11.根据cookie name 查找
#
#方法：driver.get_cookie(cookie_name)
#
#实例：driver.get_cookie("NET_SessionId")
#
#12.截取当前页面
#
#方法：
#
#get_screenshot_as_file(filename)
#实例：driver.
#get_screenshot_as_file("D:\\Program Files\\Python27\\NM.bmp")
#13.获取当前窗口的坐标
#方法：get_window_position()
#实例：driver.get_window_position()
#14.获取当前窗口的长和宽
#方法：get_window_size()
#实例：driver.get_window_size()
#
#
#
#
#
#
#新建实例driver = webdriver.Chrome()
#
#1.获取当前页面的Url函数
#
#方法：current_url
#
#实例：
#
#driver.current_url
#
#2.获取元素坐标
#
#方法：location
#
#解释：首先查找到你要获取元素的，然后调用location方法
#
#实例：
#
#driver.find_element_by_xpath("//*[@id='tablechart']/tbody/tr[14]/td[9]").location
#
#3.表单的提交
#
#方法：submit
#
#解释:查找到表单（from）直接调用submit即可
#
#实例：
#
#driver.find_element_by_id("form1").submit()
#
#4.获取CSS的属性值
#
#方法：value_of_css_property(css_name)
#实例：
#driver.find_element_by_css_selector("input.btn").value_of_css_property("input.btn")
#5.获取元素的属性值
#方法：get_attribute(element_name)
#实例：
#driver.find_element_by_id("sellaiyuan").get_attribute("sellaiyuan")
#6.判断元素是否被选中
#方法：is_selected()
#实例：
#driver.find_element_by_id("form1").is_selected()
#7.返回元素的大小
#方法：size
#实例：
#driver.find_element_by_id("iptPassword").size
#返回值：{'width': 250, 'height': 30}
#8.判断元素是否显示
#方法：is_displayed()
#实例：
#driver.find_element_by_id("iptPassword").is_displayed()
#9.判断元素是否被使用
#方法：is_enabled()
#实例：
#driver.find_element_by_id("iptPassword").is_enabled()
#10.获取元素的文本值
#方法：text
#实例：driver.find_element_by_id("iptUsername").text
#11.元素赋值
#方法：send_keys(*values)
#实例：
#driver.find_element_by_id("iptUsername").send_keys('admin')
#注意如果是函数需要增加转义符u,eg.
#driver.find_element_by_id("iptUsername").send_keys(u'青春')
#12.返回元素的tagName
#方法：tag_name
#实例：
#driver.find_element_by_id("iptUsername").tag_name
#13.删除浏览器所以的cookies
#方法：delete_all_cookies()
#实例：
#driver.delete_all_cookies()
#14.删除指定的cookie
#方法：delete_cookie(name)
#实例：deriver.delete_cookie("my_cookie_name")
#15.关闭浏览器
#方法：close()
#实例：driver.close()
#16.关闭浏览器并且推出驱动程序
#方法：quit()
#实例：driver.quit()
#17.返回上一页
#方法：back()
#实例：driver.back()
#18.设置等待超时
#方法：implicitly_wait(wait_time)
#实例：driver.implicitly_wait(30)
#19.浏览器窗口最大化
#方法：maximize_window()
#实例：driver.maximize_window()
#20.查看浏览器的名字
#方法：name
#实例：drvier.name

