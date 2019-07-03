from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from halls import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('explore/', views.explore, name='explore'),

    #AUTH
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # Hall
    path('hollaffame/create', views.CreateHall.as_view(), name="create_hall"),
    path('hollaffame/<int:pk>', views.DetailHall.as_view(), name="detail_hall"),
    path('hollaffame/<int:pk>/update', views.UpdateHall.as_view(), name="update_hall"),
    path('hollaffame/<int:pk>/delete', views.DeleteHall.as_view(), name="delete_hall"),

    # Video
    path('hollaffame/<int:pk>/addvideo', views.Add_video, name="add_video"),
    path('video/<int:pk>/delete', views.DeleteVideo.as_view(), name="delete_Video"),
    path('video/search', views.video_search, name="video_search"),
    # handler404 = 'mco.views.handler404'
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'halls.views.handler404'

