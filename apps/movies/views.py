import os
import urllib.request

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from TopMessage.settings import BASE_DIR
from apps.movies import models


# Create your views here.


def get_session(request):
    return request.session.get("user_id")


def logout(request):
    request.session["user_name"] = ''
    request.session["user_id"] = ''
    request.session["usertype"] = ''
    return render(request, 'login.html')


def image_init():
    movies = models.MovieInfo.objects.all()
    for movie in movies:
        file_path = os.path.join(BASE_DIR, "static", "image")
        img_url = movie.image
        file_name = movie.url_object_id
        try:
            if movie.image_path:
                if not os.path.exists(os.path.join(file_path, movie.image_path)):
                    file_suffix = os.path.splitext(img_url)[1]
                    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
                    urllib.request.urlretrieve(img_url, filename=filename)
                    print(filename)
                    movie.image_path = image_path
                    movie.save()
                else:
                    print("exists")
            else:
                file_suffix = os.path.splitext(img_url)[1]
                filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
                urllib.request.urlretrieve(img_url, filename=filename)
                image_path = '{}{}'.format(file_name, file_suffix)
                movie.image_path = image_path
                movie.save()
                print(image_path)
        except:
            print("failed")
    print(file_path)


def login(request):
    if get_session(request):
        return HttpResponseRedirect("/movies_form")
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            password = request.POST.get('password')

            if models.User_list.objects.filter(user_id=user_id).exists():
                user = models.User_list.objects.get(user_id=user_id)
                if password == user.userpassword:
                    request.session["user_id"] = user.user_id
                    request.session["user_name"] = user.user_name
                    request.session["usertype"] = user.usertype
                    request.session.set_expiry(5000)
                    return HttpResponseRedirect("/movies_form")
                else:
                    return render(request, 'login.html', {'message': '用户密码错误'})
            else:
                return render(request, 'login.html', {'message': '用户不存在'})
    return render(request, 'login.html')


def movies_form(request):
    if get_session(request):
        pass
    else:
        return HttpResponseRedirect("/login")
    user_id = request.session["user_id"]
    user_name = request.session["user_name"]
    user_fav = models.User_favorite.objects.all().filter(user_id=user_id)
    movies = models.MovieInfo.objects.all().order_by('top')

    if request.method == 'POST':
        movie_id = request.POST.get("movie_id")
        if not user_fav.filter(url_object_id=movie_id).exists():
            models.User_favorite.objects.create(user_id=user_id, url_object_id=movie_id)
        else:
            user_fav.filter(url_object_id=movie_id).delete()
        print(movie_id)

    paginator = Paginator(movies, 25)
    current_page = int(request.GET.get('page', 1))
    if paginator.num_pages > 7:
        if current_page - 3 < 1:
            page_ran = range(1, 8)
        elif current_page + 3 > paginator.num_pages:
            page_ran = range(paginator.num_pages - 6, paginator.num_pages + 1)
        else:
            page_ran = range(current_page - 3, current_page + 4)
        page_range = page_ran
    else:
        page_range = paginator.page_range
    current_page_content = paginator.page(current_page)
    return render(request, 'movies_form.html', {
        "movies": current_page_content,
        "page_range": page_range,
        "user_fav": user_fav,
        "user_name": user_name
    })


def register(request):
    if get_session(request):
        return HttpResponseRedirect("/movies_form")
    else:
        if request.method == 'GET':
            return render(request, 'register.html')
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            if models.User_list.objects.filter(user_id=user_id).exists():
                return render(request, 'register.html', {'message': '用户已存在'})
            else:
                if password != repassword:
                    return render(request, 'register.html', {'message': '密码不一致'})
                else:
                    models.User_list.objects.create(user_id=user_id, user_name=user_id, userpassword=password,
                                                    usertype="user")
                    if models.User_list.objects.filter(user_id=user_id).exists():
                        return render(request, 'register.html', {'message': '注册成功'})
                    else:
                        return render(request, 'register.html', {'message': '注册失败请联系管理员'})
    return render(request, 'register.html')


def user_setting(request):
    if get_session(request):
        pass
    else:
        return HttpResponseRedirect("/login")
    user_id = request.session["user_id"]
    if request.method == 'POST':
        print("post")
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        user = models.User_list.objects.get(user_id=user_id)

        if user_name:
            print("rename")
            user.user_name = user_name
            user.save()
            request.session["user_name"] = user.user_name
            return render(request, 'user_setting.html', {'message': '改名成功'})
        elif password:
            print("repass")
            if password != repassword:
                return render(request, 'user_setting.html', {'message': '密码不一致'})
            else:
                user.userpassword = password
                user.save()
                return render(request, 'user_setting.html', {'message': '修改成功'})
    else:
        print("failed")
    return render(request, 'user_setting.html')


def user_favorite(request):
    if get_session(request):
        pass
    else:
        return HttpResponseRedirect("/login")
    user_id = request.session["user_id"]
    user_name = request.session["user_name"]
    user_fav = models.User_favorite.objects.all().filter(user_id=user_id)
    movies = models.MovieInfo.objects.all().order_by('top')

    if request.method == 'POST':
        movie_id = request.POST.get("fav")
        if user_fav.filter(url_object_id=movie_id).exists():
            user_fav.filter(url_object_id=movie_id).delete()
    return render(request, 'user_favorite.html', {
        "user_name": user_name,
        "user_fav": user_fav,
        "movies": movies,
    })
