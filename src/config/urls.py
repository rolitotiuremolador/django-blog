from django.contrib import admin
from django.urls import path, include
from app_homepage import views as homepage_views
from app_accounts import views as account_views
# from app_forum import views as forum_views

urlpatterns = [
    path('admin/', admin.site.urls),

#homepage
    path('', homepage_views.home, name='home'),

#forum
    path('forum/', include('app_forum.urls')),

#accounts
    path('signup/', account_views.signup, name='signup'),
]
