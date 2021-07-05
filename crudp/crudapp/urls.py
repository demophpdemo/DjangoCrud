from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "app"

urlpatterns = [
    path('',views.index,name="index"),
    path('employeer/show/',views.show,name="show"),
    path('employeer/update/<int:id>',views.update,name="update"),
    path('employeer/delete/<int:id>/',views.delete,name="delete"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)