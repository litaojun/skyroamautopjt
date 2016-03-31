#!/usr/bin/env python
# encoding: utf-8
from skyroamautopjt.sim.SelenuieWeb import SelenuieWeb
def getObjByTagName(partenObj,mothName,curTagname):
        csstag = SelenuieWeb.cssTagList.getEelementByTagName(curTagname)
        try:
              methonRef = getattr(partenObj,mothName)
        except AttributeError:
              print "元素没有该方法"
              raise
        except:
              tagDesption = SelenuieWeb.cssTagList.getElmByDestion(curTagname)
              print tagDesption+"---------------------------------------------------------元素未找到"
              raise
        try:
              a = methonRef(curTagname)
        except NoSuchElementException:
              tagDesption = SelenuieWeb.cssTagList.getElmByDestion(curTagname)
              print tagDesption+"---------------------------------------------------------元素未找到"
              raise
        except:
              print "erro"
              raise
#智能等待
def waitElementByTime(curdriver,driver,mothName,pathstr):
        methonRef = getattr(driver,mothName)
        wait = WebDriverWait(curdriver,30)
        elm = wait.until(lambda x: x(pathstr))
        elm.click()

