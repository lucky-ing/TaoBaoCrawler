# -*- coding: UTF-8 -*-
# file: main.py
# author: Lucky-ing
# time: 21/11/2017
# Copyright 2017 Lucky-ing. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

from urllib import request
import re,time
from tqdm import tqdm
from selenium import webdriver
from bs4 import BeautifulSoup
class download_picture(object):
    def __init__(self,args):
        self.args=args
        self.nummax=int(self.args.nummax)
        if self.args.filepath[-1]!='/':
            self.args.filepath+='/'
    def start_core(self):
        drive = webdriver.Firefox(executable_path='./utils/geckodriver')
        drive.get('http://www.taobao.com')

        time.sleep(0.5)
        jpg=re.compile(r'.*(\.jpg).*')
        if drive.find_element_by_tag_name('input'):
            inp=drive.find_element_by_tag_name('input')
            inp.clear()
            inp.send_keys(self.args.keyword)
            search=drive.find_element_by_tag_name('button').click()
            flag=1
        else:
            print('error!')
        t = 0
        j='error'
        q=0
        while(t<self.nummax):
            try:
                time.sleep(0.1)
                bs = BeautifulSoup(drive.page_source, 'lxml')
                for i in bs.find_all('div',class_='items'):
                    if len(i.find_all('div',class_='item J_MouserOnverReq  '))<1:
                        continue
                    q += 1
                    for z in tqdm(i.find_all('div',class_='item J_MouserOnverReq  '),desc=str(q)+'st batch:'):
                        j=z.find('img')
                        t = t + 1
                        if j.has_attr('src'):
                            a=re.findall(jpg,j['src'])
                            if len(a)>0:
                                #print(j['src'])
                                request.urlretrieve('http:'+j['src'],self.args.filepath+self.args.keyword+str(t)+'.jpg')
                                #print(j['src'])
                                time.sleep(0.1)
                        else:
                            if j.has_attr('data-src'):
                                a = re.findall(jpg, j['data-src'])
                                if len(a) > 0:
                                    #print(1)
                                    request.urlretrieve('http:' + j['data-src'], self.args.filepath+self.args.keyword + str(t) + '.jpg')
                                    #print(j['data-src'])
                                    time.sleep(0.1)
                j=drive.find_element_by_xpath("//a[@class='J_Ajax num icon-tag']")
                if j:
                    j.click()
                else:
                    break
            except:
                print(j)

        drive.close()