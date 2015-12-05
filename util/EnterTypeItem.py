#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
from skyroamautopjt.util.readExecl import operExcel
import config
reload(sys)
sys.setdefaultencoding('utf8')

class EnterTypeItem:
    def __init__(self,formEnterType,curValue,browser):
        self.browser=browser
        self.formEnterType=formEnterType
        self.curValue=curValue
        self.getTypeByFormItem()
        if curValue is not None and curValue != '':
             #print 'curValue====' + curValue
             self.enterItemByType()
    def getSelectList(self):
        rstlist = []
        if self.itemType == 'select':
            templ = self.getDictBySelectList()
            rstlist = templ[0]
            print "start----------rstlist========="+str(rstlist)
            templ[1][templ[0][0]].click()
        #self.formEnterType.find_element_by_css_selector("img[class=\"x-form-trigger x-form-arrow-trigger\"]").click()
        return rstlist
    def getEelementValue(self):
          itemvalue=''
          if self.itemType == 'textarea':
               itemvalue = self.formEnterType.find_element_by_css_selector("textarea").get_attribute("value")
               print "textarea="+itemvalue
          else:
              if self.itemType == 'input' or self.itemType == 'select' :
                    itemvalue = self.formEnterType.find_element_by_css_selector("input[type=\"text\"]").get_attribute("value")
                    print "input="+itemvalue
          return itemvalue.strip()
    def getEelementClass(self):
          itemvalue=''
          if self.itemType == 'textarea':
               itemvalue = self.formEnterType.find_element_by_css_selector("textarea").get_attribute("class")
               print "textarea="+itemvalue
          else:
              if self.itemType == 'input' or self.itemType == 'select' :
                    itemvalue = self.formEnterType.find_element_by_css_selector("input[type=\"text\"]").get_attribute("class")
                    print "input="+itemvalue
          return itemvalue.strip()
    def getTypeByFormItem(self):
        try:
          self.formEnterType.find_element_by_css_selector("img[class=\"x-form-trigger x-form-arrow-trigger\"]")
          time.sleep(1)
        except  NoSuchElementException,e:
           try:
              self.formEnterType.find_element_by_css_selector("input")
           except:
             self.itemType="textarea"
           else:
             self.itemType="input"
        else:
           self.itemType="select"
    def enterTextareaItem(self):
        self.formEnterType.find_element_by_css_selector("textarea").clear()
        self.formEnterType.find_element_by_css_selector("textarea").send_keys(self.curValue)
        time.sleep(1)
    def enterInputItem(self):
        self.formEnterType.find_element_by_css_selector("input").clear()
        self.formEnterType.find_element_by_css_selector("input").send_keys(self.curValue)
        time.sleep(1)
    def enterSelectItem_bak(self):
        time.sleep(1)
        self.formEnterType.find_element_by_css_selector("img[class=\"x-form-trigger x-form-arrow-trigger\"]").click()
        time.sleep(1)
        listapn=self.browser.find_elements_by_css_selector("div[class=\"x-layer x-combo-list \"]:last-child>div.x-combo-list-inner>div[class*=\"x-combo-list-item\"]")
        print "listapn="+str(len(listapn))
        print "---------start"
        for item in listapn:
            print "item.text="+item.text+"-----curValue="+self.curValue
            #print dir(item)
            #print "item.innerHTML"+item.innerHTML
            time.sleep(0.05)
            if item.text.strip() == self.curValue:
                item.click()
                break;
        time.sleep(1)
        print "---------end"
    def enterSelectItem(self):
          allitem = self.getDictBySelectList()
          if self.curValue in allitem[0]:
              #print "111111111111111111111----111111111"
              allitem[1][self.curValue].click()
              #print "111111111111111111111----222222"
          else:
              print  "选择输入框，需要选择的项" + self.curValue + "在选择列表中不存在！"
              #当输入的值在LIST中不存在始，调用该方法处理，传入参数1 输入的值，2 下拉列表中第一个值对应的对象
              self.selectListNofount(self.curValue,allitem[1][allitem[0][0]])
          time.sleep(1)
          print "---------end"
    def getDictBySelectList(self):
         rstdict={}
         rstlist=[]
         self.formEnterType.find_element_by_css_selector("img[class=\"x-form-trigger x-form-arrow-trigger\"]").click()
         listitem=self.browser.find_elements_by_css_selector("div[class=\"x-layer x-combo-list \"]:last-child>div.x-combo-list-inner>div[class*=\"x-combo-list-item\"]")
         for item in listitem:
             rstdict[item.text.strip()] = item
             rstlist.append(item.text.strip())
         print "rstdict="+str(rstdict)
         print "rstlist="+str(rstlist)
         return rstlist,rstdict
    def compareSelectList(self,*args):
          allitem = self.getDictBySelectList()
          assert args == allitem[0]
    def enterItemByType(self):
        if self.curValue is None or self.curValue == '':
            print "不需要修改或新增为空的项--------a"
            return
        print "self.curValue="+self.curValue
        if self.itemType == "input":
            self.enterInputItem()
        else:
            if self.itemType == "select":
                self.enterSelectItem()
            else:
                self.enterTextareaItem()
    def  selectListNofount(self,curvalue,item):
         #根据config配置文件的配置值来决定如何处理
         if config.noexitsSelect == 1 :
             raise SelectListException(curvalue)
         else:
             item.click()
             #innerHTML
class SelectListException(Exception):  
    def __init__(self, curvalue):  
        self.curvalue = curvalue
        print  "选择输入框，需要选择的项" + self.curValue + "在选择列表中不存在！"
if __name__ == "__main__":
      aa = operExcel(u'E:\kankan\VaCache\页面元素CSS标签.xlsx',u'用户管理')
      aa.getSheetDataList()
      aa.initElementData()
      aa.printData()
