from rest_framework import routers
from .views import CategoryCreateReadDeleteView

router = routers.DefaultRouter()
router.register('category', CategoryCreateReadDeleteView, 'category')

urlpatterns = router.urls