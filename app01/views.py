from django.shortcuts import render, HttpResponse

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


