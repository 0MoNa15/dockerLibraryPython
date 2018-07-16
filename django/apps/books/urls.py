from django.conf.urls import url, include

#from . import views
from apps.books.views import CreateBooks

urlpatterns = [
    #path('', views.Index, name='index'),
    url(r'^$', CreateBooks.as_view(), name="create_books_url"),

]