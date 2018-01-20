from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
       path('', views.index, name='index'), 
       path('books/', views.BookListView.as_view(), name='books'),  
       path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),  

]
urlpatterns += [   
    path('mybooks/',views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

#this is from the form module section urls.
urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
