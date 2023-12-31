from django.urls import path
from . import views
from .views import TodoList,TodoDetail,DetailView,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
    path("",TodoList.as_view(),name="list"),
    path("detail/<int:pk>",TodoDetail.as_view(),name="detail"),
    path("create/",TodoCreate.as_view(),name="create"),
    path("update/<int:pk>",TodoUpdate.as_view(),name="update"),
    path("delete/<int:pk>",TodoDelete.as_view(),name="delete"),
]