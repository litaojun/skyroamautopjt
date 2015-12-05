#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from skyroamautopjt.util.EnterTypeItem import EnterTypeItem
from skyroamautopjt.sim.SelenuieWeb import SelenuieWeb,getObjByTagName
from skyroamautopjt.sim.AddSim import AddSim
from skyroamautopjt.util.readExecl import elementTabLayout
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class UpdateCharge(AddSim):
    def __init__(self):
        SelenuieWeb.__init__(self)
        self.addlayout = elementTabLayout(u'E:\kankan\VaCache\页面布局\套餐管理\套餐资费信息.xlsx',u'修改资费')
        self.addlayout.initElementData()
    def select_One_Charge(self,chargeItem):
        allcharge = getObjByTagName(self.browser,"find_elements_by_css_selector",'packagemanage00007')
        for curchge in allcharge:
            a = getObjByTagName(curchge,"find_element_by_css_selector",'packagemanage00008').text
            b = getObjByTagName(curchge,"find_element_by_css_selector",'packagemanage00009').text
            c = getObjByTagName(curchge,"find_element_by_css_selector",'packagemanage00010').text
            tmpcge = [a,b,c]
            print "tmpcge==="+str(tmpcge)
            if tmpcge == chargeItem:
                getObjByTagName(curchge,"find_element_by_css_selector",'packagemanage00008').click()
                return
        print "选择的资费信息不存在，退出"
        assert 1 == 2
    def getAddsimWin(self):
         xx=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00014')
         return xx
    def click_Save(self):
            getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00012')[0].click()
            time.sleep(3)
            #allbutt="body>div[class=\" x-window x-window-plain x-window-dlg\"] td[class=\"x-toolbar-cell\"] button"
            #ybtObj = self.browser.find_elements_by_css_selector(allbutt)
            ybtObj = getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00013')
            ybtObj[0].click()
            time.sleep(1)
    def check_Result(self,rstTxt):
       #textTag="body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-ml span"
        #textTagObj=self.browser.find_element_by_css_selector(textTag)
        textTagObj=getObjByTagName(self.browser,'find_element_by_css_selector','packagemanage00005')
        curtext = textTagObj.text
        #if rstTxt == curtext:
        #    print "check pass"
        #else:
        #   print "check fail"
        assert  rstTxt == curtext
        #okBtTag="body>div[class=\" x-window x-window-plain x-window-dlg\"] button"
        #okobj=self.browser.find_element_by_css_selector(okBtTag)
        okobj=getObjByTagName(self.browser,'find_element_by_css_selector','packagemanage00006')
        okobj.click()
        time.sleep(10)
     

if __name__ == "__main__":
    #charge = ChargeMgr()
    a=UpdateCharge()
    cgritem=['120','HKD',u'小时']
    a.login_Skyroam_Web("admin","111111")
    print "start-----------------------"
    a.select_Menu_Item("套餐管理","资费管理")
    a.select_One_Charge(cgritem)
    a.enter_One_SimItem(u'价格','120')
    a.enter_One_SimItem(u'货币类型','HKD')
    a.enter_One_SimItem(u'单位',u'小时')
    a.click_Save()
    a.check_Result("operated succesfully!")
    a.close_Browser()