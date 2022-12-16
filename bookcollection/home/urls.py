from django.urls import path
from .views import index, Category, Signup, Login

urlpatterns = [
    path('', index, name='homepage'),
    path('category', Category.as_view(), name='categories'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view())

]
