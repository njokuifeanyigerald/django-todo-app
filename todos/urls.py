from django.urls import path
from .views import todo_home, todo_details, todo_add, todo_edit, todo_delete
app_name = "todos"
urlpatterns = [
    path('', todo_home, name="todo_home"),
    path('ed/<int:id>/',todo_edit, name="todo_edit" ),
    path('del/<int:id>/',todo_delete, name="todo_delete" ),
    path('details/<int:id>/',todo_details, name="todo_details" ),
    path('add_todo/',todo_add, name="todo_add" ),
]
