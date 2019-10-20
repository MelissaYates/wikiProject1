from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login_user/', views.login_user, name="login_user"),
    path('new_user/', views.new_user, name="new_user"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('search_box/', views.search_box, name="search_box"),
    path('delete_article/<int:id>/', views.delete_article, name="delete_article"),
    path('individual_entry/<int:id>/', views.individual_entry, name="individual_entry"),
    path('new_wiki_entry/', views.new_wiki_entry, name="new_wiki_entry"),
    path('related_posts/', views.related_posts, name="related_posts"),
    path('all_wiki/', views.all_wiki, name="all_wiki"),
    path('display_results/', views.display_results, name="display_results"),
    path('logout_user/', views.logout_user, name="logout_user"),
]