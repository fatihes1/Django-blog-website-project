"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
#upload files aşağı 
from django.conf import settings
from django.conf.urls.static import static


from article import views # Article klasörü --modeli-- içindeki index fonksiyonunu içeri aldık
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), # import edilen fonk anasayfaya gidince çağrılacak -----  name="index" sayesinde başka bir yerde redirect fonk ile indexi çağırabilir hale gelecez
    path('about/', views.about, name="about"),
    path('articles/',include("article.urls") ), #article klasöründeki urls.py ile bağlantı
    # yukarıdaki path article gördükten sonra article klasörü içindeki urls.py ye yönlenip devam edecek
    path('user/', include("user.urls")),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)