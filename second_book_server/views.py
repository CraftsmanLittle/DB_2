from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from second_book_server.models import *
from second_book_server.tests import *
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.db.models import Min,Avg,Max,Sum,Count
import time
import os

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        username = data.get('nickname')
        password = data.get('password')
        university = data.get('university')
        admin = data.get('admin')
        print(email)
        find_same = User.object.filter(email = email)
        print(find_same)
        if len(find_same) > 0:
            if admin:
                return JsonResponse({"data": "failure"}, safe=False)
            else:
                return render(request, 'register.html')
        else:
            User.object.create_user(email = email,username=username,password = password,university=university)
            if not admin:
                return redirect('/log')
            else:
                return JsonResponse({"data": "success"}, safe=False)

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        is_user = User.object.filter(email = email)
        print(is_user)
        if is_user:
            user = authenticate(email=email, password=password)
            if user is not None:
                auth.login(request,user)
                if user.is_admin == True:
                    return redirect("/admin_index")
                else:
                    return redirect('/index')
            else:
                return render(request,'login.html')
        else:
            return render(request, 'login.html')

def index(request):
    if request.user.is_authenticated:
        name = request.user.user_nickname;
        return render(request,'index.html',{"is_auth":"True","username":name})
    else:
        return render(request,'index.html',{"is_auth":"False"})


#活动的详情的战士页面的响应，请求包含活动名称，返回的时候根据特定的名称进行响应
def activity(request):
    if request.method == 'GET':
        return render(request,'activity.html')
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        resultObject = Activity.objects.get(activity_id= activity_id)
        result = model_to_dict(resultObject)
        return JsonResponse(result,safe=True)

#公告的详情的界面响应，请求会返回所有的公告的内容
def announcement(request):
    if(request.method == 'GET'):
        return render(request,"announcement.html")
    if(request.method == 'POST'):
        json_list = []
        announcementObject = Announcement.objects.all()
        for announcement in announcementObject:
            json_data = model_to_dict(announcement)
            json_list.append(json_data)
        return JsonResponse(json_list,safe=False)

#商品的详情界面响应，返回的商品的详细信息这个商品的评价信息
def goods(request):
    if(request.method == 'GET'):
        goods_id = request.GET.get("goods_id")
        goodsObject = Goods.objects.get(goods_id=goods_id)
        goodsResult = model_to_dict(goodsObject)
        bookImage = {}
        bookImage['iamge'] = "static/goods/"+str(goodsResult['goods_id'])+"/"+goodsResult['goods_name']+".jpg"
        bookImage['iamge1'] = "static/goods/" + str(goodsResult['goods_id']) + "/" + goodsResult['goods_name'] + "1.jpg"
        bookImage['iamge2'] = "static/goods/" + str(goodsResult['goods_id']) + "/" + goodsResult['goods_name'] + "2.jpg"
        return render(request,'goods.html',{"goods_id":goods_id,"bookImage":bookImage})
    if(request.method == 'POST'):
        goods_id = request.POST['goods_id']
        print(goods_id)
        goodsObject = Goods.objects.get(goods_id = goods_id)
        goodsResult = model_to_dict(goodsObject)
        bookObject = Book.objects.get(bool_id= goodsResult['book_id'])
        print(bookObject)
        bookResult = model_to_dict(bookObject)
        jsonlist = []
        jsonlist.append(goodsResult)
        jsonlist.append(bookResult)
        commentObject = User_comment.objects.filter(goods_id=goods_id)
        for comment in commentObject:
            json_data = model_to_dict(comment)
            user = User.object.get(id = json_data['user_id'])
            userResult = model_to_dict(user)
            json_data['user_id'] = userResult['user_nickname']
            jsonlist.append(json_data)
        return JsonResponse(jsonlist, safe=False)

#商品的列表
def goods_list(request):
    type = request.GET.get('type')
    print(type)
    if type == "所有商品":
        listObject = Goods.objects.filter()
    else:
        listObject = Goods.objects.filter(subject=type)
    jsonlist = []
    for listitem in listObject:
        json_data = model_to_dict(listitem)
        jsonlist.append(json_data)
    return JsonResponse(jsonlist, safe=False)

#商家发布商品的界面
def publish(request):
    if request.method == "GET":
        return render(request,"publish.html")
    if request.method == "POST":
        form = request.POST
        print(form)
        book = Book.objects.create(book_name = form["book_name"],
                            publish_time = form["book_publish_date"],
                            book_version = form["book_vertion"],
                            author = form["book_author"],
                            author_introduction = form["book_information"],
                            publish_house = form["book_publisher"])
        #bookresult = model_to_dict(book)
        times = time.localtime(time.time())
        formattime = time.strftime("%Y-%M-%d %H:%M",times)
        good = Goods.objects.create(
            goods_id=2,
            user_id = User.object.filter(id = form["user_id"])[0],
            book_id = book,
            goods_name = form["book_name"],
            goods_time = formattime,
            goods_price = form["book_price"],
            goods_price1 =  form["book_price1"],
            introduction = form["book_introduction"],
            subject = form["book_type"],
            amount = form["book_amount"],)
        good.url = "static/goods/2/心理学与生活.jpg"
        good.save()
        s = {"goods_id":good.goods_id}
        return JsonResponse(s,safe=False)

#卖家界面
def seller(request):
    if request.method == "GET":
        return HttpResponse("这是卖家界面！")

@csrf_exempt
def upload(request):
    if request.method == 'GET':
        return render(request,"image.html")
    if request.method == 'POST':
        goods_id = request.POST.get('goods_id')
        new_img = IMG(
            img=request.FILES.get('img'),
            name=goods_id+request.FILES.get('img').name
        )
        good = Goods.objects.get(goods_id=goods_id)
        good.url = new_img.url
        goods.save()
        new_img.save()
    return HttpResponse("上传成功")

#管理员发布活动界面
def admin_activity(request):
    return render(request,"admin-activity.html")

#管理员发布公告界面
def admin_anno(request):
    return render(request,"admin-anno.html")

#管理员发布优惠券界面
def admin_coupon(request):
    if request.method == "GET":
        return render(request,"admin-coupon.html")
    else:
        form = request.POST
        coupon = Coupon.objects.create(
            coupon_name = form["name"],
            credits = form["credits"],
            begin_time = form["start_time"],
            end_time = form["end_time"]
        )
        coupon.save()
        return HttpResponse("你好")

#管理员管理货物界面
def admin_goods(request):
    return render(request,"admin-goods.html")

#g管理员的默认界面
def admin_index(request):
    '''
    data = dict()
    data['amount'] = 4333
    data['amount_rate'] = "增长了 31%"
    data["ordersheet_num"] = 2333
    data["ordersheet_rate"] = "下降了 5.2%"
    data['user_num'] = 350
    data['user_rate'] = "增加了 25 人"
    # 最近订单
    latest_order_list = []
    for x in range(0, 10):
        latest_order = dict()
        latest_order['username'] = 'Peter'
        latest_order['goods_name'] = "Database System"
        latest_order['order_sheet_state'] = "delivering"
        latest_order['order_sheet_time'] = "2018/12/18"
        latest_order['order_sheet_id'] = "12178 20181214 0533"
        latest_order_list.append(latest_order)
    data['latest_order_sheet'] = latest_order_list
    # 返回的json格式
    repos = {"data": data, "code": 200, "error_msg": ""}
    return render(request, "admin-index.html", repos)
    return HttpResponse("OK")
    '''
    if request.method == "GET":
        data = dict()
        money = Ordersheet.objects.all().aggregate(Sum("final_price"))
        data['amount'] = money["final_price__sum"]
        ammount = Ordersheet.objects.all().aggregate(Count("order_id"))
        data["ordersheet_num"] = ammount["order_id__count"]
        number = User.object.all().aggregate(Count("email"))
        data['user_num'] = number["email__count"]
        latest_order_list = []
        orders = Ordersheet.objects.all()
        for order in orders:
            a = model_to_dict(order)
            a["goods_id"] = order.goods_id.goods_name
            latest_order_list.append(a)
        data['latest_order_sheet'] = latest_order_list
        print(data)
        repos = {"data": data, "code": 200, "error_msg": ""}
        return render(request,"admin-index.html",repos)

#管理员管理用户界面
def admin_user(request):
    return render(request,"admin-user.html")


#聊天界面
def chat(request):
    if request.method == 'GET':
        temp_id = request.GET.get('goods_id')
        buyer_email = request.user.email
        print(buyer_email)
        seller_email = Goods.objects.get(goods_id=temp_id).user_id
        buyer_name = User.object.get(email =buyer_email).user_nickname
        seller_name = seller_email.user_nickname
        seller_email = 2;
        repos = dict()
        repos['my_eamil'] = buyer_email
        repos['my_nickname'] = buyer_name
        repos['target_email'] = seller_email
        repos['target_nickname'] = seller_name
        print(repos)
        return render(request, "chat.html", repos)

    return render(request,"chat.html")

#用户优惠券界面
def mycoupon(request):
    user_id = request.user.id
    coupons = User_coupon.objects.filter(user_id = user_id)

    index = ["name","end_time","amount"]
    final = []
    for coupon in coupons:
        result = []
        result.append(coupon.Coupon_id.coupon_name)
        result.append(coupon.Coupon_id.end_time)
        result.append(coupon.ammount)
        b = dict(zip(index, result))
        final.append(b)
    return render(request,"mycoupon.html",{"result":final})

#卖家商品界面
def mygoods(request):
    user_id = request.user.id
    goods = Goods.objects.filter(user_id = user_id)
    result = []
    for good in goods:
        a = model_to_dict(good)
        result.append(a)
    return render(request,"mygoods.html",{"mygoods":result})

#我的订单界面
def myorder(request):
    user_id = request.user.id
    orders = Ordersheet.objects.filter(buyer_id=user_id)
    final = []
    index = ["order_id","date","state","final_price","goods_name","version","publish_house","type","url"]
    for order in orders:
        result = []
        result.append(order.order_id)
        result.append(order.date)
        result.append(order.state)
        result.append(order.final_price)
        result.append(order.goods_id.goods_name)
        result.append(order.goods_id.book_id.book_version)
        result.append(order.goods_id.book_id.publish_house)
        result.append(order.goods_id.subject)
        result.append(order.goods_id.url)
        b = dict(zip(index,result))
        final.append(b)
    return render(request,"myorder.html",{"items":final})

#订单删除页
def order_delete(request):
    order_id = request.GET["order_id"]
    order = Ordersheet.objects.filter(order_id = order_id).delete()
    return redirect("/myorder")

#提交订单界面
def ordersheet(request):
    if request.method == "GET":
        address = User_address.objects.get(user_id= request.user.id)
        addressresult = model_to_dict(address)
        seller_id = Goods.objects.get(goods_id= request.GET.get("goods_id")).user_id
        coupon_id = User_coupon.objects.filter(user_id = request.user.id)
        couponResult = []
        for coupon in coupon_id:
            a = model_to_dict(coupon)
            couponResult.append(a["Coupon_id"])
        coupon_filter = Coupon.objects.filter(Coupon_id__in = couponResult)
        couponResult1 = []
        for name in coupon_filter:
            couponResult1.append(name)
        return render(request, "ordersheet.html",{"goods_id":request.GET.get("goods_id"),"seller_id":seller_id,"address":addressresult,
                                                  "coupon":couponResult1})
    else:
        form = request.POST
        coupon_ids = form["coupon"].split()
        coupon_id = int(coupon_ids[1])
        price1 = Goods.objects.get(goods_id=form["goods_id"]).goods_price1
        price2 = Coupon.objects.get(Coupon_id = coupon_id).credits
        final_price = price1 - price2
        times = time.localtime(time.time())
        formattime = time.strftime("%Y-%M-%d %H:%M", times)
        sheet = Ordersheet.objects.create(
            buyer_id=request.user.id,
            Seller_id=form["seller"],
            state="等待卖家确认",
            is_paid=True,
            goods_id=Goods.objects.get(goods_id=form["goods_id"]),
            name = form["name"],
            note = form["note"],
            phonenumber=form["phonenumber"],
            coupon_id = Coupon.objects.get(Coupon_id = coupon_id),
            final_price=final_price,
            date = formattime
        )
        sheet.save()
        return redirect("/myorder")

#个人信息页
def profile(request):
    a = model_to_dict(User.object.get(id = request.user.id))
    print(a)
    return render(request,"profile.html",{"user":a})

#验证页
def validation(request):
    if request.method == "GET":
        user_id = request.user.id
        return render(request,"validation.html")

    if request.method == "POST":
        form = request.POST
        print(request.user.id)
        print(form)
        user = User.object.get(id = request.user.id)
        user.email = form["email"]
        user.university = form["unniversity"]
        user.user_nickname = form["nickname"]
        user.user_profile = form["profile"]
        user.password = form["password"]
        user.save()
        auth.login(request, user)
        return JsonResponse({"data": "success"}, safe=False)

#注销页
def logout(request):
    auth.logout(request)
    return redirect("/index")

def pubanno(request):
    form = request.POST
    times = time.localtime(time.time())
    formattime = time.strftime("%Y-%M-%d", times)
    anno = Announcement.objects.create(
        an_title=form["title"],
        type = form["type"],
        an_content = form["content"],
        date = formattime,
    )
    anno.save()
    return HttpResponse("OK")

def admin_anno_list(request):
    if request.method == 'GET':
        repos = []
        annos = Announcement.objects.all()
        for anno in annos:
            a = model_to_dict(anno)
            repos.append(a)
        '''
        for x in range(0, 10):
            data = dict()
            data['anno_id'] = "4396" + str(x)
            data['anno_title'] = "大猩猩"
            data['anno_type'] = "新闻资讯"
            data['anno_publish_time'] = "2018/12/18"
            repos.append(data)
        '''
        return JsonResponse(repos, safe=False)


def admin_search_anno(request):
    if request.method == 'POST':
        anno_id = request.POST.get('anno_id')
        data = dict()
        data = model_to_dict(Announcement.objects.get(an_id=anno_id))
        return JsonResponse(data, safe=False)

def admin_anno_delete(request):
    if request.method == 'POST':
        anno_id = request.POST.get('anno_id')
        Announcement.objects.filter(an_id=anno_id).delete()
        return JsonResponse({})

def admin_activity_delete(request):
    if request.method == 'POST':
        anno_id = request.POST.get('activity_id')
        Activity.objects.filter(activity_id=anno_id).delete()
        return JsonResponse({})

def admin_activity_list(request):
    if request.method == "GET":
        repos = []
        activitys = Activity.objects.all()
        for activity in activitys:
            b = model_to_dict(activity)
            repos.append(b)
        return JsonResponse(repos, safe=False)

def admin_publish_activity(request):
    if request.method == "POST":
        form = request.POST
        ac = Activity.objects.create(
            activity_name= form["name"],
            content=form["goods_id"],
            begin_time=form["start_time"],
            end_time=form["end_time"],
            pecent=form["activity_price"]
        )
        ac.save()
        list = form["goods_id"]
        l = list.split('/')
        print(l)
        for item in l:
            price1 = Goods.objects.get(goods_id=item).goods_price1
            good = Goods.objects.get(goods_id=item)
            good.goods_price1 = price1 * float(form["activity_price"])
            good.save()
        return JsonResponse({"data":"success"})

def admin_search(request):
    result = []
    email = request.POST['searched_user']
    a = User.object.get(email = email)
    b = model_to_dict(a)
    result.append(b)
    return JsonResponse(result,safe=False)

def admin_user_list(request):
    users = User.object.filter()
    result = []

    for user in users:
        a = model_to_dict(user)
        a["register_time"] = user.register_time
        result.append(a)
    print(result)
    return JsonResponse(result, safe=False)

def admin_user_delete(request):
    User.object.filter(id =request.POST["username"]).delete()
    return JsonResponse({})

def admin_user_latest_login(request):
    users = User.object.filter().order_by('last_login')
    count = 0
    repos = []
    for user in users:
        if count == 8:
            break
        a = model_to_dict(user)
        a["register_time"] = user.register_time
        repos.append(a)
    return JsonResponse(repos,safe=False)

def delete_goods(request):
    goods_id = request.POST["goods_id"]
    Goods.objects.filter(goods_id=goods_id).delete()
    return JsonResponse({})

def shopping_cart(request):
    if request.method == "GET":
        user_id = request.user.id
        shop_cars = Shopping_cart.objects.filter(user_id=user_id)
        total_price = 0
        total_amount = 0
        totol_type_amount = 0

        result = []
        for shop_car in shop_cars:
            totol_type_amount += totol_type_amount
            a = model_to_dict(shop_car)
            total_amount += shop_car.amount
            total_price += shop_car.price * shop_car.amount
            a["image_url"] = shop_car.goods_id.url
            a["goods_name"] = shop_car.goods_id.goods_name
            result.append(a)

        repos = {"data":result,"total_price":total_price,"total_num":total_amount,"goods_type_num":totol_type_amount}
        return JsonResponse(repos,safe=False)

def search(request):
    key = request.POST["key"]
    goods = Goods.objects.filter(goods_name__contains=key)

    result = []
    for good in goods:
        a = model_to_dict(good)
        result.append(a)

    return JsonResponse(result,safe=False)

def admin_publish(request):
    return render(request,"admin-goods-publish.html")
