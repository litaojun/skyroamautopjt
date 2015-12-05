#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from skyroamautopjt.util.EnterTypeItem import EnterTypeItem
from skyroamautopjt.util.readExecl import elementTabLayout
from AddSim import AddSim
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from SelenuieWeb import SelenuieWeb,getObjByTagName
class UpdateSim(AddSim):
    def __init__(self):
        SelenuieWeb.__init__(self)
        #super(self).__init__(self)
       #(u'E:\kankan\VaCache\页面布局\sim卡管理\sim卡信息.xlsx',u'新增sim卡')
       #(u'E:\kankan\VaCache\页面布局\sim卡管理\sim卡信息.xlsx',u'修改SIM卡')
        self.addlayout = elementTabLayout(u'E:\kankan\VaCache\页面布局\sim卡管理\sim卡信息.xlsx',u'修改SIM卡')
        self.addlayout.initElementData()
    def getAddsimWin(self):
        xx=getObjByTagName(self.browser,"find_elements_by_css_selector",'packagemanage00011')
        return xx
if __name__ == "__main__":
        a=UpdateSim()
        a.login_Skyroam_Web("admin","111111")
        print "start-----------------------"
        a.select_Menu_Item("SIM卡管理","SIM卡信息")
        print "end-----------------------"
        a.select_Sim("084906003291549620")
        a.enter_One_SimItem(u'电话号码:','13818181818')
        a.enter_One_SimItem(u'通信技术:',u'都支持')
        a.enter_One_SimItem('PIN1:','123456')
        a.enter_One_SimItem('PIN2:','12345688')
        print a.get_One_Seletct_List(u'网络制式:')
        a.enter_One_SimItem(u'网络制式:','GSM')
        a.enter_One_SimItem(u'服务类型:',u'数据短信')
        