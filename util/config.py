#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
from skyroamautopjt.util.readExecl import operExcel
reload(sys)
sys.setdefaultencoding('utf8')
#用户在选择下拉框后，用户输入的值在下拉列表中找不到，配置在该情况下程序如何处理
noexitsSelect = 1    #1 ：直接抛出异常         0: 选择第一个值。 