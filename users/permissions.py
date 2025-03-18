# class IsAuthenticatedOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated or request.method in permissions.SAFE_METHODS
