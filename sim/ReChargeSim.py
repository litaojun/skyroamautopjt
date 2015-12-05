#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from skyroamautopjt.util.EnterTypeItem import EnterTypeItem
import time
import sys
from AddSim import AddSim
reload(sys)
sys.setdefaultencoding('utf8')
from SelenuieWeb import SelenuieWeb,getObjByTagName
class ReChargeSim(SelenuieWeb):
    cssTagList = None
    def __init__(self):
        #super(type(SelenuieWeb),self).__init__()
        SelenuieWeb.__init__(self)
        pass
    def select_ReCharge_Sim(self,simiccid):
        #curtag="body>div[class=\" x-panel x-border-panel\"] div.x-column-inner>div[class=\" x-portal-column x-column\"]>div[class=\" x-panel x-portlet\"]:first-child"
        #temptag=self.browser.find_element_by_css_selector(curtag)
        temptag=getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00020')
        print "1111111111111"
        #listSim=temptag.find_elements_by_css_selector("div.x-grid3-viewport>div.x-grid3-scroller>div.x-grid3-body>div.x-grid3-row ")
        listSim=getObjByTagName(temptag,'find_elements_by_css_selector','usermanage00021')
        print "2222222222222--len(listSim)="+str(len(listSim))
        for cursim in listSim:
            print "1111111111111"
            temp=cursim.find_elements_by_css_selector("td")[3]
            if temp.text.strip() == simiccid:
                print "1111111111111--temp.text"+temp.text
                temp.click()
                break
    def enter_ReCharge_Win(self):
        #buttontag="body>div[class=\" x-panel x-border-panel\"] div[class=\" x-portal-column x-column\"]>div[class=\" x-panel x-portlet\"] div[class=\"x-toolbar x-small-editor x-toolbar-layout-ct\"] td.x-toolbar-right button"
        #print "len(buttontag)="+str(len(buttontag))+"--buttontag[0]"+str(buttontag[0])
        #self.browser.find_element_by_css_selector(buttontag).click()
          getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00022').click()
    def enter_Money_Save(self,rmbValue):
        time.sleep(1)
        textmonstr="body>div[class=\" x-window x-resizable-pinned\"] input[class=\" x-form-text x-form-field\"]"
        svbuttonstr = "body>div[class=\" x-window x-resizable-pinned\"] button"
        #self.browser.find_element_by_css_selector(textmonstr).send_keys("100")
        getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00023').send_keys("100")
        time.sleep(1)
        #self.browser.find_element_by_css_selector(svbuttonstr).click()
        getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00024').click()
        allbuttonstr = "body>div[class=\" x-window x-window-plain x-window-dlg\"] button"
        #allbutton=self.browser.find_elements_by_css_selector(allbuttonstr)
        allbutton=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00025')
        print "allbutton-len=",len(allbutton)
        curtxet={item.text.strip():item for item in allbutton}
        curtxet['yes'].click()
        #allbutton[0].click()
    def check_ReCharge_Result(self,gjrst):
        resultstr="div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-ml span.ext-mb-text"
        #rstobj=self.browser.find_element_by_css_selector(resultstr)
        rstobj=getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00026')
        #if rstobj.text.strip() == gjrst:
        #   print "check success"
        #else:
        #   print "check fail"
        assert rstobj.text.strip() == gjrst
        okbuttonstr="div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-bl button"
        #allbuttonobj=self.browser.find_elements_by_css_selector(okbuttonstr)
        allbuttonobj=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00027')
        curtxet={item.text.strip():item for item in allbuttonobj}
        curtxet['OK'].click()
if __name__ == "__main__":
    a=ReChargeSim()
    a.login_Skyroam_Web("admin","111111")
    print "start-----------------------"
    a.select_Menu_Item("SIM卡管理","SIM卡余额&明细")
    a.select_ReCharge_Sim("898600921912a9813835")
    a.enter_ReCharge_Win()
    a.enter_Money_Save("100")
    a.check_ReCharge_Result("operated succesfully!")
    a.close_Browser()