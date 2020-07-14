from django.urls import path, include
from .views import approvereject, ApprovalsViewSet, cxcontact
from rest_framework import routers
router = routers.DefaultRouter()
router.register('MyAPI', ApprovalsViewSet)

urlpatterns = [
    path('form/', cxcontact, name='myform'),
    path('api/', include(router.urls), name='api'),
    path('status/', approvereject, name='status'),
]



