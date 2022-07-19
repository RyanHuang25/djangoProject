from django.shortcuts import render,HttpResponse
import requests
from lxml import etree
# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    name = 'huangrenwu'
    roles = ['CEO','爬虫工程师','后端开发']
    user_info = {
        "name": "huangrenwu",
        "age": 18,
        "job": "爬虫工程师"
    }
    return render(request,'user_list.html',{"n1": name,'roles': roles,"user_info": user_info})

def user_add(request):
    return HttpResponse('添加用户')

def news(request):
    url = 'https://www.163.com/dy/media/T1603594732083.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    res = requests.get(url,headers=headers)
    tree = etree.HTML(res.text)
    url = tree.xpath("//div[@class='desc']/h4/a/@href")[0]
    res = requests.get(url,headers=headers)
    tree = etree.HTML(res.text)
    newsList = tree.xpath("//div[@class='post_body']/p[2]/text()")
    titleList = newsList[:2]
    newsList = newsList[2:]
    return render(request,'news.html',{"newsList": newsList,"titleList": titleList})