from rest_framework import permissions

class isSuperUser(permissions.BasePermission):
    def has_permissions(self, request, view):
        if request.method == 'DELETE':
            if request.user.if_superuser:
                return True
            return False
        return True