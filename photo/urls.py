from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import photo
from photo.views import PhotoCreate, PhotoDelete, PhotoUpdate, PhotoDetail, PhotoList

app_name = 'photo'

urlpatterns = [
    path('create/', PhotoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),
    path('', PhotoList.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
