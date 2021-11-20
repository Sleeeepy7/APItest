# class BasePermission(object):
#     """ Базовый класс от которого идут все разрешения для правки/просмотра api юзерами """
#
#     def has_permission(self, request, view):
#         """ Возвращает правду если разрешение имеется"""
#
#         return True
#
#     def has_object_permission(self, request, view, obj):
#         """ Возвращает правду если все права имеются """
#
#         return True

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """ Только читать доступны для любых запросов"""
        if request.method in permissions.SAFE_METHODS:
            return True
        """ Добавлять статьи доступны для автору поста"""
        return obj.author == request.user
