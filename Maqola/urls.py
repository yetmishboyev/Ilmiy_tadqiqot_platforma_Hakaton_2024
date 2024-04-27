from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('',Sayt.as_view()),
    path('qidirish/',Dashboard.as_view()),
    path('izlash/',Qidiruv.as_view()),
    path('form/',Forms.as_view()),
    path('wikipediya/',Wikipediya.as_view()),
    path('tr/',Translete.as_view()),
    # path('diagramma/',Charts.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
