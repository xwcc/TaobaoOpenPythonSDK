#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 推荐词
# @author wuliang@maimiaotech.com
# @date 2012-06-12 20:50:52
# @version: 0.0.0

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())


                                
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">推荐词</SPAN>
class RecommendWord(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">平均价格</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Private</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.average_price = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">相关度</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Private</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.pertinence = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">搜索量</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Private</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.pv = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">推荐的关键词</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Private</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.word = None
        
        self.__init(kargs)
        
    def _newInstance(self, name, value):
        propertyType = self._getPropertyType(name)
        if propertyType == bool:
            return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            return datetime.strptime(value, format)
        elif propertyType == str:
            return value.encode("utf-8")
        else:
            return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "average_price": "String",
            
            "pertinence": "String",
            
            "pv": "String",
            
            "word": "String",
        }
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(
                sys.modules[os.path.basename(
                os.path.dirname(os.path.realpath(__file__))) + "." + nameType], 
                nameType)
        return pythonType
        
    def __init(self, kargs):
        
        if kargs.has_key("average_price"):
            self.average_price = self._newInstance("average_price", kargs["average_price"])
        
        if kargs.has_key("pertinence"):
            self.pertinence = self._newInstance("pertinence", kargs["pertinence"])
        
        if kargs.has_key("pv"):
            self.pv = self._newInstance("pv", kargs["pv"])
        
        if kargs.has_key("word"):
            self.word = self._newInstance("word", kargs["word"])
