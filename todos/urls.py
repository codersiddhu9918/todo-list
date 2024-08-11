from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('main/',views.todo_list, name="main"),
    # path('insert_todo/',views.insert_todo_items,name="insert"),
    # path('delete_todo/<int:todo_id>',views.delete_todo_items, name="delete"),
    # # path('',views.ulogin,name="login"),
    # path('user_login',views.us_login,name="user_login"),
    path('',views.TaskList.as_view(),name='tasks'),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task_create'),
    path('task-edit/<int:pk>', views.TaskUpdate.as_view(), name='task_edit'),
    path('task-delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
    path('login/', views.customLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register')
    # path('logout/',views.logout,name="logout"),
    # path('register',views.register,name="register")
]