from django.urls import path
from . import views

app_name = 'crazy_book_clubs'

urlpatterns = [
    path('',views.index, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/reviews/', views.book_reviews, name='book_reviews'),
    path('books/new/', views.new_book, name='new_book'),
    path('books/<int:book_id>/reviews/new/', views.new_review, name='new_review'),
    path('reviews/<int:review_id>/edit/', views.edit_review, name='edit_review'),
]

