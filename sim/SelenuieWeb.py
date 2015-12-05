#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from skyroamautopjt.util.EnterTypeItem import EnterTypeItem
from skyroamautopjt.util.readExecl import operExcel
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class SelenuieWeb:
    cssTagList = None
    def __init__(self):
            print "xxxxx"
            #cssTagList = None
            if  SelenuieWeb.cssTagList is None:
                   SelenuieWeb.cssTagList = operExcel(u'E:\kankan\VaCache\页面元素CSS标签.xlsx',u'用户管理')
                   #temptag = operExcel(u'E:\kankan\VaCache\页面元素CSS标签.xlsx',u'套餐管理')
                   #SelenuieWeb.cssTagList.elementData = SelenuieWeb.cssTagList.elementData + temptag.elementData
                   print 'type(SelenuieWeb.cssTagList)==='+str(type(SelenuieWeb.cssTagList))
                   print 'type(SelenuieWeb.cssTagList)==='+str(type(self.__class__.cssTagList))
    def login_Skyroam_Web(self,username,password):
        #for a in curPara.keys():
            #self.browser.find_element_by_name(a).send_keys(curPara[a])
        #time.sleep(1)
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.1.103:8080/boss-web/index.jsp')
        self.browser.maximize_window()
        self.simItem=['11112222111522','21111222',u'澳门CTM','01','澳门CTM','澳门CTM','都支持','WCDMA','数据短信','待分配','99999','999999299999','123456','9','GMT+8','1121111101111','111111','111111','111111','111111','sssss']
        #self.simItemUd=['',None,'26189996',u'澳门CTM','01',u'澳门CTM',u'澳门CTM',u'都支持',u'数据短信','WCDMA',u'待分配','99999','123456','9','GMT+8','1121111101111','111111','111111','111111','111111','sssss']
        self.simItemUd=None
        #self.browser.find_element_by_name("j_usernamea").send_keys(username)
        getObjByTagName(self.browser,'find_element_by_name',"usermanage00004").send_keys(username)
        #self.browser.find_element_by_name("j_password").send_keys(password)
        getObjByTagName(self.browser,'find_element_by_name',"usermanage00005").send_keys(password)
        time.sleep(1)
        #print self.browser.getHtmlSource()
        self.browser.find_element_by_name("submit").submit()
        time.sleep(1)
    def select_Menu_Item(self,menunum,menuname):
        #allmenus = self.browser.find_elements_by_css_selector("body>div[class=\" x-panel x-border-panel\"] div[class=\"x-tree-root-node\"]>li[class=\"x-tree-node\"]")
        allmenus = getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00006')
        print "allmenus="+str(len(allmenus))
        selMenu = None
        for curmenu in allmenus:
            if curmenu.text.strip() == menunum:
                selMenu=curmenu
                break
        #selMenu.find_element_by_css_selector("img[class=\"x-tree-ec-icon x-tree-elbow-plus\"]").click()
        getObjByTagName(selMenu,'find_element_by_css_selector','usermanage00002').click()
        time.sleep(1)
        selMenu.find_element_by_link_text(menuname).click()
        time.sleep(1)
    def select_Sim(self,simnum):
        #allsim = self.browser.find_elements_by_css_selector("body>div[class=\" x-panel x-border-panel\"] div.x-grid3-viewport>div.x-grid3-scroller>div.x-grid3-body>div[class=\"x-grid3-row \"]")
        allsim = getObjByTagName(self.browser,"find_elements_by_css_selector",'usermanage00007')
        print "allsim="+str(len(allsim))
        cursim=None
        for x in allsim:
            print "find sim start"+x.find_elements_by_tag_name("td")[3].text.strip()
            if x.find_elements_by_tag_name("td")[3].text.strip() == simnum:
                print "find sim success"
                cursim=x
                break
        #alltd=allsim[simnum].find_elements_by_tag_name("td")
        #print "alltd="+str(len(alltd))+"---alltd[4].text=="+alltd[4].text
        cursim.find_elements_by_tag_name("td")[3].click()
    def get_All_SimItem(self):
        xx=getObjByTagName(self.browser,"find_elements_by_css_selector",'usermanage00008')
        rstList=[]
        for item in range(len(xx)):
            rstList.append(EnterTypeItem(xx[item],'',self.browser).getEelementValue())
        return rstList
    
    def edit_Sim_Save(self,*updateSimItem):
        xx=getObjByTagName(self.browser,"find_elements_by_css_selector",'usermanage00008')
        self.simItemUd = updateSimItem
        print "updateSimItem==len==" + str(len(updateSimItem))
        for item in range(len(xx)):
            curTypeItem=EnterTypeItem(xx[item],self.simItemUd[item],self.browser)
        nowhandle=self.browser.current_window_handle
        self.browser.find_element_by_css_selector("div.x-panel-bl button:nth-child(2n+1)").click()
        time.sleep(1)
        allhandles=self.browser.window_handles
        print "99999---00000-1==="+str(len(allhandles))
        for myhandle in allhandles:
            if myhandle != nowhandle:
                print "99999---00000-2"
                self.browser.switch_to_window(myhandle)
                self.browser.find_element_by_link_text("yes").click()
                self.browser.switch_to_window(nowhandle)
                break
        try:
           #alertwin=self.browser.find_element_by_css_selector("div[class=\" x-window x-window-plain x-window-dlg\"] td[class=\"x-toolbar-cell\"] button[class=\" x-btn-text\"]:nth-child(n+1)")
           alertwin=getObjByTagName(self.browser,"find_element_by_css_selector",'usermanage00009')
        except NoSuchElementException,ex:
           print "alertwin not found"
           print Exception,":",ex
        else:
           alertwin.click()
        print "99999---00000-3"
        #xxy=self.browser.find_element_by_css_selector("div[class=\" x-window x-window-plain x-window-dlg\"] td[class=\"x-toolbar-cell\"] button[class=\" x-btn-text\"]:nth-child(n+1)")
        #xxy=getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00010')
        #if xxy is not None:
        #   print "99999---00000-4"
        #   xxy.click()
    def update_Sim_Save_Button(self):
         self.browser.find_element_by_css_selector("div.x-panel-bl button:nth-child(2n+1)").click()
         time.sleep(1)
         alertwin=getObjByTagName(self.browser,"find_element_by_css_selector",'usermanage00009')
         alertwin.click()
    def open_AddSim_Win(self):
        #mybutton=self.browser.find_elements_by_css_selector("div[class=\" x-panel x-border-panel\"] div[class=\"x-toolbar x-small-editor x-toolbar-layout-ct\"] button")
        mybutton=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00011')
        print "mybutton.len="+str(len(mybutton))+"mybutton[0].text="+mybutton[0].text
        mybutton[0].click()
        time.sleep(1)
    def enter_Sim_Item(self,*simItemContent):
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
        #buttonNums=self.browser.find_elements_by_css_selector("div[class=\" x-window x-resizable-pinned\"]>div.x-window-bwrap>div.x-window-bl div[class=\"x-panel-fbar x-small-editor x-toolbar-layout-ct\"] button")
        buttonNums=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00015')
        buttonNums[0].click()
        time.sleep(1)
        #buttonyess=self.browser.find_elements_by_css_selector("body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-bl tr.x-toolbar-left-row>td[class=\"x-toolbar-cell\"] button")
        buttonyess=getObjByTagName(self.browser,'find_elements_by_css_selector','usermanage00016')
        print "buttonyess="+str(len(buttonyess))+"---buttonyess[0].text="+buttonyess[0].text
        buttonyess[0].click()
        time.sleep(1)
    def check_Test_Result(self,desptions):
        resultText=self.browser.find_element_by_css_selector("body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-ml span.ext-mb-text").text
        print "resultText="+resultText
        if resultText == desptions:
             print "check pass"
             assert 1 == 1
        else:
            print "check fail"
            assert 1 == 2
        self.browser.find_element_by_css_selector("body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap>div.x-window-bl button").click()
        if resultText != "operated succesfully!":
            buttonNums=self.browser.find_elements_by_css_selector("div[class=\" x-window x-resizable-pinned\"]>div.x-window-bwrap>div.x-window-bl div[class=\"x-panel-fbar x-small-editor x-toolbar-layout-ct\"] button")
            print "buttonNums[2].text="+buttonNums[2].text
            buttonNums[2].click()
            print "xxx"
    def check_AlertSim_Result_text(self,desptions):
         #abstr = "body>div[class=\" x-window x-window-plain x-window-dlg\"]>div.x-window-bwrap span.ext-mb-text"
         tsstr = getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00028').text
         assert tsstr == desptions
         xxy=getObjByTagName(self.browser,'find_element_by_css_selector','usermanage00010')
         if xxy is not None:
            print "99999---00000-4"
            xxy.click()
    def close_Browser(self):
        self.browser.quit()
    def test_Fun(self):
        print "litaojun"
    def check_two_data(self,a,*b):
        print "a=============="+str(a)
        print "b=============="+str(b)
        x = tuple(a)
        assert x == b
    def check_Sim_Data(self,*yqlist):
         #actlist = self.get_All_SimItem()
         if len(yqlist) != 2:
             print "yqlist=======2"
             assert 1 == 2
         check_AlertSim_data(yqlist[0],yqlist[1])
    def check_Sima_Data(self,*yqlist):
         actlist = self.get_All_SimItem()
         check_AlertSim_data(actlist,yqlist)
def check_AlertSim_data(actlist,yqlist):
          if actlist == None or len(actlist) == 0:
              assert 1 == 2
          assert len(actlist) == len(yqlist)
          for x in range(len(actlist)):
              if yqlist[x] != '' and yqlist[x] != None:
                  print "actlist[x]="+actlist[x]+",yqlist[x]="+yqlist[x]
                  assert actlist[x] == yqlist[x]

def getObjByTagName(partenObj,mothName,curTagname):
        print 'type(SelenuieWeb.cssTagList)==='+str(type(SelenuieWeb.cssTagList))
        csstag = SelenuieWeb.cssTagList.getEelementByTagName(curTagname)
        a=None
        print "csstag===========" + csstag + "结束"
        try:
              methonRef = getattr(partenObj,mothName)
        except AttributeError:
              print "元素没有该方法"
              raise
        except:
              tagDesption = SelenuieWeb.cssTagList.getElmByDestion(curTagname)
              print tagDesption+"000---------------------元素未找到"
              raise
        try:
              a = methonRef(csstag)
        except NoSuchElementException:
              print "type(SelenuieWeb.cssTagList)===="+type(SelenuieWeb.cssTagList)
              tagDesption = SelenuieWeb.cssTagList.getElmByDestion(curTagname)
              print tagDesption+"--------------------------元素未找到"
              raise
        except:
              print "erro"
              raise
        return a

if __name__ == "__main__":
    a=SelenuieWeb()
    a.login_Skyroam_Web("admin","111111")
    print "start-----------------------"
    a.select_Menu_Item("SIM卡管理","SIM卡信息")
    print "end-----------------------"
    #a.open_AddSim_Win()
    #a.enter_Sim_Item('11112222111522','21331222','澳门CTM','01','澳门CTM','澳门CTM','都支持','WCDMA','数据短信','待分配','99999','999999299999','123456','9','GMT+8','1121111101111','111111','111111','111111','111111','sssss')
    a.select_Sim("084906003291549620")
    a.edit_Sim_Save()
    a.check_Test_Result("operated succesfully!")
    a.close_Browser()
