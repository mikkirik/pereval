from django.urls import include, path
from rest_framework import routers
from .views import SubmitData

router = routers.DefaultRouter()
router.register('submitData', SubmitData)

urlpatterns = [
    path('', include(router.urls)),
]
