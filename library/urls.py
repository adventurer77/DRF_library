"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# from main.views import CategoryViewSet, BookViewSet, AuthorViewSet, AuthorAPIUpdate, AuthorAPIDetailViev


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("main.urls")),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("api/v1/booklist/", BookViewSet.as_view()),

#     path("api/v1/authorlist/", AuthorViewSet.as_view()),
#     path("api/v1/authorlist/<int:pk>/", AuthorAPIUpdate.as_view()),
#     path("api/v1/authordetail/<int:pk>/", AuthorAPIDetailViev.as_view()),

#     path("api/v1/categorylist/", CategoryViewSet.as_view({"get": "list"})),
#     path("api/v1/categorylist/<int:pk>/", CategoryViewSet.as_view({"put": "update"}))
# ]