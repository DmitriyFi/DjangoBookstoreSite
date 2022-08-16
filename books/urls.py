from django.urls import path

from .views import BookListView, BookDetailView, ReviewCreateView, ReviewDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<uuid:pk>/new/', ReviewCreateView.as_view(), name='review_new'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
