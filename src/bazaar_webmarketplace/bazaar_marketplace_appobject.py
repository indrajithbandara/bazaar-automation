#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
#encoding:utf-8

from selenium import webdriver
import threading ,ConfigParser


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
                instance = webdriver.Chrome()
                #instance = webdriver.Ie()
            else:  
                print u" Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            mutex.release()  
    else:  
            print u" Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
    return instance  
    
    
    
conf = ConfigParser.ConfigParser()
conf.read("C:/BazaarCodeDeveloper/bazaarworkspace/bazaar-automation/test-config/userdata_bazaarweb.conf")

global bazaarwebhostname,bazaarwebusername,bazaarwebpassword
bazaarwebhostname = conf.get("bazaarwebsection", "uihostname")
bazaarwebusername = conf.get("bazaarwebsection", "uiusername")
bazaarwebpassword = conf.get("bazaarwebsection", "uipassword")

print bazaarwebhostname, bazaarwebusername, bazaarwebpassword


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

#test15

#define some golobal variables.  Xpath and CSS Selector 
 #operation system testcase01 perminssion manage module appobject
permloginClickButton="div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
clickPermissionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
clickPermissionButton="div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success"
    

    
 
    
    