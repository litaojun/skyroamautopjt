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
class ChargeMgr(AddSim):
    def __init__(self):
        SelenuieWeb.__init__(self)
        self.addlayout = elementTabLayout(u'E:\kankan\VaCache\椤甸潰甯冨眬\濂楅绠＄悊\濂楅璧勮垂淇℃伅.xlsx',u'鏂板璧勮垂')
        self.addlayout.initElementData()
    def enter_NewCharge_Win(self):
        #addbut = self.browser.find_element_by_css_selector("div[class=\" x-panel x-border-panel\"] div[class=\" x-portal-column x-column\"]>div[class=\" x-panel x-portlet\"]>div.x-panel-bwrap div[class=\"x-panel-tbar x-panel-tbar-noheader\"] button")
        addbut = getObjByTagName(self.browser,'find_element_by_css_selector','packagemanage00001')
        addbut.click()
    def input_Charge_Item_Sv(self,*chargeItem):
        #items = self.browser.find_elements_by_css_selector("body>div[class=\" x-window x-resizable-pinned\"]>div.x-window-bwrap div[class=\"x-form-item \"]")
        items = getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00002')
        for i in range(len(items)):
            EnterTypeItem(items[i],chargeItem[i],self.browser)
        #savebut = "body>div[class=\" x-window x-resizable-pinned\"]>div.x-window-bwrap>div.x-window-bl button"
        #self.browser.find_elements_by_css_selector(savebut)[0].click()
        getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00003')[0].click()
        time.sleep(3)
        #allbutt="body>div[class=\" x-window x-window-plain x-window-dlg\"] td[class=\"x-toolbar-cell\"] button"
        #ybtObj = self.browser.find_elements_by_css_selector(allbutt)
        ybtObj = getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00004')
        ybtObj[0].click()
        time.sleep(1)
    def click_Save(self):
        getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00003')[0].click()
        time.sleep(3)
        #allbutt="body>div[class=\" x-window x-window-plain x-window-dlg\"] td[class=\"x-toolbar-cell\"] button"
        #ybtObj = self.browser.find_elements_by_css_selector(allbutt)
        ybtObj = getObjByTagName(self.browser,'find_elements_by_css_selector','packagemanage00004')
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
        time.sleep(2)
    def view_ChargeItem(self):
        pass
    def alter_Charge_Save(self):
        pass
if __name__ == "__main__":
    #charge = ChargeMgr()
    a=ChargeMgr()
    cgritem=["11",'CNY','灏忔椂','ssssssssssss']
    a.login_Skyroam_Web("admin","111111")
    print "start-----------------------"
    a.select_Menu_Item("濂楅绠＄悊","璧勮垂绠＄悊")
    a.enter_NewCharge_Win()
    a.enter_One_SimItem(u'浠锋牸','120')
    a.enter_One_SimItem(u'璐у竵绫诲瀷','HKD')
    a.enter_One_SimItem(u'鍗曚綅',u'灏忔椂')
    a.click_Save()
    #a.input_Charge_Item_Sv(cgritem)
    a.check_Result("operated succesfully!")
    a.close_Browser()