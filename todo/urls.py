from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',views.TodoViewSetApiView)

urlpatterns = [
    
    path('', views.todo_all),
    path('<int:todo_id>', views.todo_all_edit_delete),
    path('cbv/', views.TodoListDataApiView.as_view()),
    path('cbv/<int:todo_id>', views.TodoSingleDataApiView.as_view()),
    path('mixins/', views.TodoListMixins.as_view()),
    path('mixins/<pk>', views.TodoSingleMixins.as_view()),
    path('aaa/', views.aaa),
    path('generic/<pk>', views.TodoDetailsGenericsApiView.as_view()),
    path('generic/', views.TodoGenericApiView.as_view()),
    path('viewsets/',include(router.urls)),
    path('user/', views.UserGenericApiView.as_view()),

]
