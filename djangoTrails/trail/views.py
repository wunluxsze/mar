from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse


def posts(request, countPosts=0):
    return HttpResponse(f"Все посты: {countPosts}")


def popular(request, countPosts=0):
    return HttpResponse(f"Популярные посты: {countPosts}")


def last(request, countPosts=0):
    return HttpResponse(f"Последние посты: {countPosts}")


def comments(request, postId=0, countComments=0):
    return HttpResponse(f"Номер поста: {postId}<br>Количество комментариев: {countComments}")


def likes(request, postId=0, countLikes=0):
    return HttpResponse(f"Пост: {postId}<br>Количество лайков: {countLikes}")


def user(request):
    login = request.GET.get("login", "none")
    password = request.GET.get("password", "none")
    return HttpResponse(f"<h2>Логин: {login} Пароль: {password}</h2>")


def about(request):
    return HttpResponseRedirect("/")


def contacts(request):
    return HttpResponsePermanentRedirect("/")


def error(request):
    return HttpResponseNotFound("Загрузка страницы была завершена ошибкой")


def access(request):
    login = request.GET.get("login", "none")
    password = request.GET.get("password", "none")
    if login == "admin" and password == "admin":
        return HttpResponse("Все норм")
    return HttpResponse("Доступ запрещен")


def json(request):
    return JsonResponse(request.GET)


def set(request):
    key = request.GET.get("key", "none")
    value = request.GET.get("value", "none")
    response = HttpResponse(f"Привет {key} {value}")
    response.set_cookie(key, value)
    return response


def get(request):
    key = request.GET.get("key", "none")
    value = request.COOKIES[key]
    return HttpResponse(f"Пока {key} {value}")