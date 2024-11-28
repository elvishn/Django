from django.urls import path, re_path, register_converter
from . import views
from . import converters
from .views import WomenCategory, TagPostList

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', TagPostList.as_view(), name='tag'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit'),
]
