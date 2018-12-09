from django.shortcuts import render,render_to_response
import  datetime
from django.http import HttpResponse
from TestModel.models import Publisher

#def hello(request):
#    return HttpResponse("Hello world!")

# 利用模板
def hello(request):
    context = {'person_name':'hhhh','company':'oooo','ship_date':datetime.date(2009,4,2),'item_list':['a','b']}
 #   return render(request,'hello.html',context)   #import render   两种方法都行
    return render_to_response('hello.html',context)  # import render_to_response

#向数据库添加数据 添加数据需要先创建对象，然后再执行 save 函数，相当于SQL中的INSERT：
def testdb(request):
    test1 = Publisher(name='w3cschool.cn')
    test1.save()
    return  HttpResponse("<p>数据添加成功！</p>")

#获取数据库内容
def hqtestdb(resquest):

 # 初始化
    response = ""
    response1 = ""
 #通过objects 这个模型管理器的all（）获得所有数据行，相当于SQL中的select * from
    list = mydb.objects.all()
# filter 相当于SQL中的where，可设置条件过滤结果
    response2 = mydb.objects.filter(id=1)
#获取单个对象
    response3 = mydb.objects.get(id=1)
#限制返回的数据 相当于SQL中的 offset 0 limit 2；
    mydb.objects.order_by('name')[0:2]
#数据排序
    mydb.objects.order_by('id')
#上面的方法可以连锁使用
    mydb.objects.filter(name="w3cschool.cn").order_by("id")
#输出所有数据
    for var in list:
        response1 += var.name + ""
    response = response1
    return HttpResponse("<p>" + response + "</p>")


#更新数据  修改数据可以使用 save() 或 update()
def gxtestdb(request):
    test1 = mydb.objects.get(id=1)
    test1.name = 'w3cschoolw3cschool教程'
    test1.save()
# 另一种方法 修改单行和 修改所有的列
#mydb.objects.filter(id=1).update(name= 'w3cschoolw3cschool教程')
#mydb.objects.all().update(name='w3cschoolw3cschool教程')

    return HttpResponse("<p>修改成功</p>")

# 删除数据库中的对象只需调用该对象的delete()方法即可：
def sctestdb(request):
    test1 = mydb.objects.get(id=9)
    test1.delete()
#删除所有行
    #mydb.objects.filter(id=1).delete()
    #mydb.objects,all().delete()
    return  HttpResponse("<p>删除成功</p>")



