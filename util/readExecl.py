#!/usr/bin/env python
# encoding: utf-8
import  xdrlib,sys,xlrd
class operExcel:
         def __init__(self,filepath,workSheet):
             data = xlrd.open_workbook(filepath)
             self.curSheet = data.sheet_by_name(workSheet)
             self.elementData = {}
             self.getSheetDataList()
             self.initElementData()
             self.printData()
             
         def getSheetDataList(self):
             nrows = self.curSheet.nrows
             datals = []
             for i in range(nrows):
                 datals.append(self.curSheet.row_values(i))
             return datals
         def initElementData(self):
             mydata = self.getSheetDataList()
             for data in mydata:
                 self.elementData[data[0]] = data[1:len(data)]
         def getEelementByTagName(self,tagname):
              return self.elementData[tagname][2]
         def getElmByDestion(self,tagname):
               return self.elementData[tagname][0]
         def printData(self):
             print str(self.elementData)
class elementTabLayout:
         def __init__(self,filepath,workSheet):
             data = xlrd.open_workbook(filepath)
             self.curSheet = data.sheet_by_name(workSheet)
             self.layoutDict = {}
         def initElementData(self):
             nrows = self.curSheet.nrows
             datals = []
             for i in range(nrows):
                 curlist = self.curSheet.row_values(i)
                 for j in range(len(curlist)/3):
                     templist = curlist[j*3:j*3 + 3]
                     datals.append(templist)
             for xing in datals:
                 if xing[0] is not None and xing[0] != '':
                     self.layoutDict[xing[0]] =xing[1:3]
             print self.layoutDict
         def getlayoutDict(self):
              return self.layoutDict
             
if __name__ == "__main__":
           #aa = operExcel('E:\kankan\VaCache\页面元素CSS标签.xlsx','用户管理')
           aa = elementTabLayout(u'E:\kankan\VaCache\页面布局\sim卡管理\sim卡信息.xlsx',u'新增sim卡')
           aa.initElementData()
           b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
           x = aa.getlayoutDict()
           print b[int(x[u'电话号码:'][0])]