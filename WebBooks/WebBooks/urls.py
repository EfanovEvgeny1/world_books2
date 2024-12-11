from django.contrib import admin
from django.urls import path
from catalog import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('books/', views.BookListView.as_view(), name='books-list'), 
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)