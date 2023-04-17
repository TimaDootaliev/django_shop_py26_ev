from rest_framework import mixins, permissions, viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryCreateReadDeleteView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        elif method in ['POST', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
    