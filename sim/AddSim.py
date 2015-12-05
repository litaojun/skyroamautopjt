#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from skyroamautopjt.util.EnterTypeItem import EnterTypeItem
from skyroamautopjt.util.readExecl import elementTabLayout
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from SelenuieWeb import SelenuieWeb,getObjByTagName
class AddSim(SelenuieWeb):
     def __init__(self):
        #super(type(SelenuieWeb),self).__init__()
        SelenuieWeb.__init__(self)
        #super(self).__init__(self)
        self.addlayout = elementTabLayout(u'E:\kankan\VaCache\页面布局\sim卡管理\sim卡信息.xlsx',u'新增sim卡')
        self.addlayout.initElementData()
        pass
     def getAddsimWin(self):
        twoWins=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00012')
        #leftwins=twoWins[0].find_elements_by_css_selector("div.x-panel-bwrap>div[class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]>div[class=\"x-form-item \"]")
        leftwins=getObjByTagName(twoWins[0],'find_elements_by_css_selector','usermanage00013')
        #rigwins=twoWins[1].find_elements_by_css_selector("div.x-panel-bwrap>div[class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]>div[class=\"x-form-item \"]")
        rigwins=getObjByTagName(twoWins[1],'find_elements_by_css_selector','usermanage00014')
        allItems=leftwins + rigwins
        return allItems
     def enter_One_SimItem(self,oneSimItem,oneValue):
         addLayoutList = self.getAddsimWin()
         if oneSimItem == '' or oneSimItem is None:
             assert 1 ==2
         i = int(self.addlayout.getlayoutDict()[oneSimItem][0])
         EnterTypeItem(addLayoutList[i],oneValue,self.browser)
     def enter_Mut_SimItem(self,mutSimItem,mutValue):
          for i in len(mutSimItem):
              enter_One_SimItem(mutSimItem[i],mutValue[i])
     def get_One_SimItem(self,oneSimItem):
         addLayoutList = self.getAddsimWin()
         if oneSimItem == '' or oneSimItem is None:
             assert 1 ==2
         i = int(self.addlayout.getlayoutDict()[oneSimItem][0])
         tmp = EnterTypeItem(addLayoutList[i],'',self.browser)
         return tmp.getEelementValue()
     def get_One_SimItemClass(self,oneSimItem):
         addLayoutList = self.getAddsimWin()
         if oneSimItem == '' or oneSimItem is None:
             assert 1 ==2
         i = int(self.addlayout.getlayoutDict()[oneSimItem][0])
         tmp = EnterTypeItem(addLayoutList[i],'',self.browser)
         classValue = tmp.getEelementClass()
         print "classValue===="+classValue
         return classValue
     def get_One_Seletct_List(self,oneSimItem):
         addLayoutList = self.getAddsimWin()
         if oneSimItem == '' or oneSimItem is None:
             assert 1 ==2
         i = int(self.addlayout.getlayoutDict()[oneSimItem][0])
         print "i============="+str(i)
         tmp = EnterTypeItem(addLayoutList[i],'',self.browser)
         print "xxxxxxxxxxx---start"
         listvalue = tmp.getSelectList()
         print "xxxxxxxxxxx---end"
         return listvalue
     def  enter_New_Simitem(self,*simItemContent):
            #twoWins=self.browser.find_elements_by_css_selector("div[class=\" x-window x-resizable-pinned\"]>div.x-window-bwrap>div.x-window-ml form[class=\"x-panel-body x-form\"] div[class=\" x-panel x-panel-noborder x-form-label-right x-column\"]")
            twoWins=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00012')
            #leftwins=twoWins[0].find_elements_by_css_selector("div.x-panel-bwrap>div[class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]>div[class=\"x-form-item \"]")
            leftwins=getObjByTagName(twoWins[0],'find_elements_by_css_selector','usermanage00013')
            #rigwins=twoWins[1].find_elements_by_css_selector("div.x-panel-bwrap>div[class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]>div[class=\"x-form-item \"]")
            rigwins=getObjByTagName(twoWins[1],'find_elements_by_css_selector','usermanage00014')
            allItems=leftwins + rigwins
            print "allitems.len="+str(len(allItems))
            for item in range(len(allItems)):
                 EnterTypeItem(allItems[item],simItemContent[item],self.browser)
                 time.sleep(1)
            print "ss"
     def  add_Win_save(self):
            buttonNums=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00015')
            buttonNums[0].click()
            time.sleep(1)
            #buttonyess=self.browser.find_elements_by_css_selector("body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-bl tr.x-toolbar-left-row>td[class=\"x-toolbar-cell\"] button")
            buttonyess=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00016')
            print "buttonyess="+str(len(buttonyess))+"---buttonyess[0].text="+buttonyess[0].text
            buttonyess[0].click()
            time.sleep(1)
     def  add_Win_not_save(self):
            buttonNums=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00015')
            buttonNums[0].click()
            time.sleep(1)
     def  add_Win_Cancel_Button(self):
            buttonNums=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00015')
            buttonNums[1].click()
            time.sleep(1)


if __name__ == "__main__":
        a=AddSim()
        a.login_Skyroam_Web("admin","111111")
        print "start-----------------------"
        a.select_Menu_Item("SIM卡管理","SIM卡信息")
        print "end-----------------------"
        a.open_AddSim_Win()
        a.enter_One_SimItem(u'电话号码:','13818181818')
        a.enter_One_SimItem(u'通信技术:',u'都支持')
        a.enter_One_SimItem('PIN1:','123456')
        a.enter_One_SimItem('PIN2:','12345688')
        print a.get_One_Seletct_List(u'网络制式:')
        a.enter_One_SimItem(u'网络制式:','GSM')
        a.enter_One_SimItem(u'服务类型:',u'数据短信')