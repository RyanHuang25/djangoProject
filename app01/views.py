from django.shortcuts import render,HttpResponse
import requests
from lxml import etree
# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    # request是一个对象，封装了用户发送过来的所有请求相关数据
    # 1.获取请求方式 GET/POST
    print(request.method)
    # 2.在url上传递值
    print(request.GET)
    # 3.在请求体中提交数据
    print(request.POST)
    # 4.【响应】HttpResponse('返回内容'),内容字符串内容返回给请求者
    # 5.【响应】读取html的内容+ 渲染（替换）-> 字符串、返回给用户浏览器
    # 6.【响应】重定向 --> return redirect("https://www.baidu.com")
    return render(request,'user_list.html',)

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