#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
#coding=utf-8

from selenium import webdriver
import threading 


#@staticmethod  
def GetInstance():  
    instance = None  
    mutex = threading.Lock() 
    if(instance == None):  
            mutex.acquire()   
            if(instance == None):  
                #printInfo(u'åˆ�å§‹åŒ–å�•ä¾‹')  
                print u"initial singleton .........."
                #instance = webdriver.Firefox()
                instance = webdriver.Ie()
                #instance = webdriver.Ie()
            else:  
                print u" Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            mutex.release()  
    else:  
            print u" Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
    return instance  
    
    
class Singleton(): 
    instance = None  
    mutex = threading.Lock()    
    def __init__(self):  
        pass  
     
    @staticmethod  
    def GetInstance():  
        if(Singleton.instance == None):  
            Singleton.mutex.acquire()   
            if(Singleton.instance == None):  
                #printInfo(u'åˆ�å§‹åŒ–å�•ä¾‹')  
                print u"initial singleton .........."
                Singleton.instance = webdriver.Firefox()
            else:  
                print u" Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            Singleton.mutex.release()  
        else:  
            print u" Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
        return Singleton.instance  

#class appobjectops:
# class appObjectUtils(self):
#     
#our testing env include test14 test15 test09    test15 is total deploy testing env, 
#test14 is pre-deploy testing env, test09 is xiaoe testing env
#test14
'''
global ops_tab_category_username,ops_tab_category_password
global ops_tab_mapSetting_subCityMapSetting,ops_tab_innertestingmanage,ops_tab_permissionmanage
global ops_tab_couponmanage,ops_tab_MarketingTools,ops_tab_freight,ops_tab_clothesmanage
global ops_tab_clothesmanage_endprice,ops_tab_clothesmanage_brand,ops_tab_clothesmanage_historyprice,ops_tab_clothesmanage_minor
global ops_tab_citymanage,ops_tab_recharge,ops_tab_distribution,ops_tab_Category,ops_tab_PriceClothes
ops_tab_permissionmanage=str(1)
ops_tab_innertestingmanage=str(2)
ops_tab_mapSetting_subCityMapSetting=str(3)
ops_tab_distribution=str(4)
ops_tab_Category=str(5)
ops_tab_Category_substation=str(3)
ops_tab_category_username="rdt10"
ops_tab_category_password="abc123"

ops_tab_PriceClothes=str(6)
ops_tab_freight=str(7)
ops_tab_clothesmanage=str(8)
ops_tab_clothesmanage_brand=str(4)
ops_tab_clothesmanage_endprice=str(2)
ops_tab_clothesmanage_historyprice=str(3)
ops_tab_clothesmanage_minor=str(1)


ops_tab_recharge=str(9)
ops_tab_citymanage=str(10)
ops_tab_couponmanage=str(11)
ops_tab_MarketingTools=str(12)
'''
#test15  XPath and CSS Selector
#operation system testcase01 perminssion manage module appobject
permloginClickButton="div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
clickPermissionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
clickPermissionButton="div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success"
    
clickPositionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
clickPositionNewButton="div#container.container div#content-container a.btn.btn-info.col-md-1"
clickPositionEditButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info"
clickPositionDeleteButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger"
    

    
 
    
    