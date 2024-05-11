from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from django.views.generic.detail import DetailView

from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormMixin

from .models import Books, Author

# Create your views here.

"""class BookListView(View):
    def get(self,request):
        book=Books.objects.all().order_by('-pk')
        return render(request,'book/book_list.html',{'book':book})
"""


class BookListView(ListView):
    model = Books
    template_name = 'book/book_list.html'
    context_object_name = 'book'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book/book_detail.html'


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('products:list')


class BookUptadeView(UpdateView):
    model = Books
    template_name = 'book/book_update.html'
    fields = ['price']

