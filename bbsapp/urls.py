from django.urls import path
from .views import signupfn, loginfn, listfn, logoutfn, detailfn, goodfn
from .views import CreatePage

urlpatterns = [
    path('signup/', signupfn, name='signup'),
    path('login/', loginfn, name='login'),
    path('list/', listfn, name='list'),
    path('logout/', logoutfn, name='logout'),
    path('detail/<int:pk>', detailfn, name='detail'),
    path('good/<int:pk>', goodfn, name='good'),
    path('create/', CreatePage.as_view(), name='create'),
]