#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:32:50 2018

@author: little_frog
"""
from selenium import webdriver###全靠这个包来搞事了
import time
import json

base_url = 'https://movie.douban.com/subject/24773958/comments?start=%d&limit=20&sort=new_score&status=P'###用来爬取的转移页面
url = 'https://movie.douban.com/subject/24773958/comments?start=0&limit=20&sort=new_score&status=P'###用来登陆的页面
sav_path = '/Users/ruicheng/Documents/上海师范研究生/python相关/爬虫/豆瓣短评爬取/result.txt'
path = '/Users/ruicheng/chromedriver01/chromedriver'
browser = webdriver.Chrome(path)

def find_cookie(name):
    browser.get(url)
    print('请登陆')
    time.sleep(30)###手动输入用户名和密码
    browser.refresh()
    cookies = browser.get_cookies()
    for cookie in cookies:
        browser.delete_all_cookies()
        browser.add_cookie(cookie)
        browser.get(url)
        html = browser.page_source
        if html.find(name)!=-1:
            return cookie
        
cookie = find_cookie(name)
browser.add_cookie(cookie)

def get_one(start):
    url = base_url%start
    browser.get(url)
    for item in browser.find_elements_by_css_selector('.comment'):
        com = {}
        #com['name'] = item.find_element_by_css_selector('.comment-info a').text###这里本想用pyquery，奈何pyquery抓不到评论，泪目QAQ
        com['text'] = item.find_element_by_css_selector('p').text
        for j in item.find_elements_by_css_selector('.comment-info span'):###elements用来找到所有的节点
            if 'allstar' in j.get_attribute('class'):
                com['grade'] = j.get_attribute('title')
        yield com

def save(results):
    for result in results:
        with open(sav_path,'a',encoding='utf-8') as f:
            f.write(json.dumps(result,ensure_ascii=False)+'\n')

for i in range(0,6):
    results = get_one(i*20)
    save(results)
    time.sleep(2)

browser.close()###最后的结尾，别忘了把浏览器驱动给关了