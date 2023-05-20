from rest_framework.permissions import BasePermission


class IsShop(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == 'shop'

    def has_object_permission(self, request, view, obj): 
        if request.method == 'GET':
            return True 
        return request.user == obj.user
         