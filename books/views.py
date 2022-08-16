from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .models import Book, Review


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    # permission_required = 'books.special_status'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'books/review_new.html'
    fields = ['review', ]
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.book_id = self.kwargs['pk']
        return super().form_valid(form)


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'books/review_delete.html'
    success_url = reverse_lazy('book_list')
