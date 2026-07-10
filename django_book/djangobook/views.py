from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

# def test(request):
#
#     return HttpResponse("OK")
from app01 import models


def home(request):
    return render(request,'home.html')

def book_list(request):
    book_queryset = models.Book.objects.all()

    return render(request,'book_list.html',locals())

def book_add(request):
    #查询所有的作者
    author_queryset = models.Author.objects.all()
    #查询所有的出版社
    publish_queryset = models.Publish.objects.all()
    if request.method == 'POST':
        #标题
        title = request.POST.get('title')
        #价格
        price = request.POST.get('price')
        #出版社日期
        publish_date = request.POST.get('publish_date')
        #出版社ID
        publish_id = request.POST.get('publish')
        #作者ID 因为有多个值 要用列表
        author_ids = request.POST.getlist('author')
        #保存数据到数据库
        book_obj = models.Book.objects.create(title=title,
                                              price=price,
                                              publish_date=publish_date,
                                              publish_id=publish_id)
        #create()会将创建的对象的返回
        #保存第三张表的数据
        #add() 可以传入多个值 *列表表示将列表打散成位置参数
        book_obj.authors.add(*author_ids)
        return redirect('book_list')
    return render(request, 'book_add.html',locals())

def book_edit(request,edit_id):
    #根据id获取图书对象
    book_obj = models.Book.objects.filter(pk=edit_id).first()
    # 查询所有的作者
    author_queryset = models.Author.objects.all()
    # 查询所有的出版社
    publish_queryset = models.Publish.objects.all()
    if request.method == 'POST':
        #标题
        title = request.POST.get('title')
        #价格
        price = request.POST.get('price')
        #出版社日期
        publish_date = request.POST.get('publish_date')
        #出版社ID
        publish_id = request.POST.get('publish')
        #作者ID 因为有多个值 要用列表
        author_ids = request.POST.getlist('author')
        #修改图书表
        book_obj.title = title
        book_obj.price = price
        book_obj.publish_date = publish_date
        book_obj.publish_id=publish_id
        #修改第三张关系表
        book_obj.authors.set(author_ids) #set() 必须传入一个可迭代对象
        book_obj.save()
        return redirect('book_list')
    return render(request,'book_edit.html',locals())

def book_delete(request,delete_id):
         #根据id直接删除
        book_obj = models.Book.objects.filter(pk=delete_id).delete()
        return redirect('book_list')


#出版社列表
def publish_list(request):
     publish_queryset = models.Publish.objects.all()
     return render(request,'publish_list.html',locals())
 #出版社添加
def publish_add(request):
    if request.method == 'POST':
            #名称
            name = request.POST.get('name')
            #地址
            address = request.POST.get('address')
            #邮箱
            email = request.POST.get('email')
            #添加数据到数据库
            models.Publish.objects.create(name=name,
                                          address=address,
                                          email=email)
            return redirect('publish_list')
    return render(request, 'publish_add.html')

 #出版社编辑
def publish_edit(request,publish_id):
     #根据id查询出版社对象
    publish_obj = models.Publish.objects.filter(pk=publish_id).first()
    if request.method == 'POST':
     # 名称
        name = request.POST.get('name')
         # 地址
        address = request.POST.get('address')
         # 邮箱
        email = request.POST.get('email')
        publish_obj.name = name
        publish_obj.address = address
        publish_obj.email = email
         #修改
        publish_obj.save()
        return redirect('publish_list')


    return  render(request,'publish_edit.html',locals())



def publish_delete(request,delete_id):
     models.Publish.objects.filter(pk=delete_id).delete()
     return redirect('publish_list')


#作者列表
def author_list(request):
         author_queryset = models.Author.objects.all()
         return render(request,'author_list.html',locals())

         # 添加作者


def author_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        # 因为要添加两张表要先拿到主表的对象 一对一
        author_obj = models.Author.objects.create(name=name, age=age)
        models.AuthorDetail.objects.create(phone=phone,
                                           addr=addr,
                                           author=author_obj)
        return render(request, 'author_list.html')

    return render(request, 'author_add.html')


 #编辑作者
def author_edit(request,author_id):
     #根据id查询出作者对象
     author_obj = models.Author.objects.filter(pk=author_id).first()
     if request.method == 'POST':
         name = request.POST.get('name')
         age = request.POST.get('age')
         phone = request.POST.get('phone')
         addr = request.POST.get('addr')
         author_obj.name=name
         author_obj.age=age
         author_obj.save()
         author_obj.authordetail.phone=phone
         author_obj.authordetail.addr=addr
         author_obj.authordetail.save()
         return redirect('author_list')
     return render(request, 'author_edit.html', locals())


 #删除
def author_delete(request,delete_id):
 models.Author.objects.filter(pk=delete_id).delete()
 return redirect('author_list')