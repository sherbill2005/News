from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, \
   ArticleUserView

urlpatterns = [
   path("", ArticleListView.as_view(), name="allArticles"),
   path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
   path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_update"),
   path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
   path("new/", ArticleCreateView.as_view(), name="article_create"),
   path("myArticles/", ArticleUserView, name="article")
]