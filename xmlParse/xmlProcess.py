#-*- coding: utf-8 -*-
import xml.sax
import sys
sys.path.append('..')
import globalData.globalData



class XmlFileHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.IP = ''
        self.Port = ''
        self.UsersNameDicPath = ''
        self.PasswordsDicPath = ''

    #元素开始事件处理
    def startElement(self, name, attrs):
        self.CurrentData = name

        return




    #元素结束事件处理
    def endElement(self, name):
        self.CurrentData = name
        if self.CurrentData == 'root':
            return

    def characters(self, content):
        if self.CurrentData == 'ip':
            self.IP = content
            global CONFIGINFO_IP
            globalData.globalData.CONFIGINFO_IP = self.IP
        elif self.CurrentData == 'port':
            global CONFIGINFO_PORT
            self.Port = content
            globalData.globalData.CONFIGINFO_PORT.append(self.Port)
        elif self.CurrentData == 'usersNameDicPath':
            self.UsersNameDicPath = content
            global CONFIGINFO_USERSNAME_PATH
            globalData.globalData.CONFIGINFO_USERSNAME_PATH = self.UsersNameDicPath
        elif self.CurrentData == 'passwordsDicPath':
            self.PasswordsDicPath = content
            global CONFIGINFO_PASSWORDS_PATH
            globalData.globalData.CONFIGINFO_PASSWORDS_PATH = self.PasswordsDicPath
        else:
            return


if (__name__ == '__main__'):
    #创建xmlReader
    parser = xml.sax.make_parser()

    Handler = XmlFileHandler()
    parser.setContentHandler(Handler)
    parser.parse('../configDoc/config.xml')










