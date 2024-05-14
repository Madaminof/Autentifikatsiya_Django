from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .forms import AddReviewForm
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import FormMixin

from .models import Books, Review

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



class Savat(BookDetailView):
    model=Books
    template_name='book/savat.html'



class AddReview(LoginRequiredMixin,View):
    def get(self,request,pk):
        books=Books.objects.get(pk=pk)
        addReview_form=AddReviewForm()
        context={
            'books':books,
            'addReview_form':addReview_form
        }
        return render(request,'book/add_review.html',context=context)

    def post(self, request, pk):
        books=Books.objects.get(pk=pk)
        addReview_form=AddReviewForm(request.POST)
        if addReview_form.is_valid():
            reviews=Review.objects.create(
                comment=addReview_form.cleaned_data['comment'],
                book=books,
                user=request.user,
                star_given=addReview_form.cleaned_data['star_given']
            )
            reviews.save()
            return redirect('products:detail', pk=pk)


class ViewReview(ListView):
    model = Review
    template_name = 'book/view_Review.html'
    context_object_name = 'view'

    def get_queryset(self):
        return Review.objects.order_by('-id')

"""
def delete_comment(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('products:list')  # Redirect to the appropriate page after deletion
    return render(request, 'confirm_delete_review.html',{'review':review})
"""


class UptadeCommentView(UpdateView):
    model = Review
    template_name = 'book/update_comment.html'
    fields = ['comment','star_given']
    success_url = reverse_lazy('products:list')




