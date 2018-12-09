import os
import  threading
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

homepage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'photo/'
parser = 'html5lib'

driver = webdriver.Firefox()
driver.get(homepage)
#print(driver.page_source)  网页的全部HTML源码
bsObj = BeautifulSoup(driver.page_source,parser)  #解析目标网页的ＨＴＭＬ源码


girlsList = driver.find_element_by_id('J_GirlsList').text.split('\n')#获得主页上所有妹纸的姓名、所在城市、身高、体重等信息
#print(girlsList)
#print(driver.find_element_by_id('J_GirlsList').text)  #后面的 split('\n') 则会将属性 text 中的字符串以换行符分割，得到一个包含所有分割后的字符串的列表


girlsUrl = bsObj.find_all("a",{"href": re.compile("\/\/.*\.htm\?(userId=)\d*")})  #解析出妹子的个人主页地址等信息

imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg',driver.page_source)  #获取所有妹子的封面图片
#print(girlsUrl)

def mkdir(path):
    #判断路径是否存在
    isExists = os.path.exists(path)
    #判断结果
    if not isExists:
        #如果不存在则创建目录
        print(" [*]新建了文件夹",path)
        #创建目录操作函数
        os.makedirs(path)
    else:
        #如果目录存在则不创建，并提示目录已存在
        print('  [+]文件夹',path,'已创建')

#所有妹纸的名字地点
girlsNL = girlsList[::3]
#print(girlsNL)
#所有妹纸的身高体重
girlsHW = girlsList[1::3]
#所有妹纸的个人主页地址
girlsHURL = [('http:' + i['href']) for i in girlsUrl]
#所有妹纸的封面图片地址
girlsPhotoURL = [('https:' + i) for i in imagesUrl]

girlsInfo = zip(girlsNL,girlsHW,girlsHURL,girlsPhotoURL)

#组装各个模块
for girlNL,girlHW,girlHURL,girlCover in girlsInfo:
    print("[*]Girl :",girlNL,girlHW)
    #为妹纸建立文件夹
    mkdir(outputDir + girlNL)
    print("   [*]saving...")
    #获取妹纸封面图片
    data = urlopen(girlCover).read()
    with open(outputDir + girlNL + '.cover.jpg','wb') as f:
        f.write(data)
    print("  [+]Loading Cover...")
    #获取妹纸个人主页中的图片
    getImgs(girlHURL,outputDir + girlNL)

def getImgs(url,path):
    driver = webdriver.Firefox(homepage)
    print("  [*]Opening...")
    bsObj = BeautifulSoup(driver.page_source,parser)
    imgs = bsObj.find_all("img",{"src": re.compile(".*\.jpg")})
    for i,img in enumerate(imgs[1:]):
        try:
            html = urlopen('https:' + img['src'])
            data = html.read()
            filename = "{ }/{ }.jpg".format(path,i + 1)
            print("   [+]Loading...", filename)
            with open(filename,'wb') as f:
                f.write(data)
        except Exception:
            print("   [!]Address Error!")
    driver.close()
















