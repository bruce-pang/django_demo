from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    # return HttpResponse('Hello, Django!')
    # 如果想要访问的是html文件请使用render、、

    # 1. 去项目根目录下的templates目录寻找index.html文件（提前先配置）【不配置就无效】
    # 2. 根据app的注册顺序，在每个app目录下的templates目录寻找index.html文件
    return render(request, 'index.html')

def user_list(request):
    # return HttpResponse('用户列表')
    # 如果想要访问的是html文件请使用render
    # 去app目录下的templates目录寻找user_list.html文件（根据app的注册顺序， 逐一去他们的templates目录寻找， 会去所有的注册的app下去找 ）
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse('添加用户')

def user_edit(request):
    return HttpResponse('编辑用户')

def user_del(request):
    return HttpResponse('删除用户')

def tpl(request):
    name = 'BrucePang'
    age = 18
    hobby = ['Java', 'Geek', 'Python']
    return render(request, 'tpl.html', {'name': name, 'age': age, 'hobby': hobby})

def news(req):
    # 定义一些新闻数据（字典或者列表） 或者 从数据库中查询新闻数据 或者爬虫爬取新闻数据
    # news_list = [
    #     {'title': '新闻1', 'content': '新闻1的内容'},
    #     {'title': '新闻2', 'content': '新闻2的内容'},
    #     {'title': '新闻3', 'content': '新闻3的内容'},
    # ]

    # 向地址： http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news  发送请求，获取网页源码，解析出新闻数据
    # 第三方模块：requests  (pip install requests)
    import requests
    #反爬虫需要加上请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 发送请求
    res = requests.get('http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news', headers=headers)
    data_list = res.json()['data']
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})

def something(request):
    # request是一个对象，封装了用户发送过来的所有请求信息
    # 1.获取请求方式 GET/POST
    print(request.method)

    # 2.获取请求值（GET）
    print(request.GET)

    # 3.获取请求体的数据（POST）
    print(request.POST)

    # 4. 响应
    # return HttpResponse('请求与响应')
    # return render(request, 'something.html', {'title': '请求与响应'}) # 5.读取html内容 + 渲染(替换) -> 字符串 -> 响应给用户浏览器

    return redirect('http://www.baidu.com') # 重定向

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 获取用户提交的数据
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username == 'admin' and password == '123456':
            # return HttpResponse('登录成功')
            return redirect('https://www.github.com/bruce-pang/prpc')
        else:
            # return HttpResponse('登录失败')
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
    else:
        return HttpResponse('请求方式错误')




