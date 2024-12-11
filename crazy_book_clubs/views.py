from django.shortcuts import render, get_object_or_404, redirect
from . models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.

def index(request):
    return render(request, 'crazy_book_clubs/index.html')

def book_list(request):
    books = Book.objects.all() 
    return render(request, 'crazy_book_clubs/book_list.html', {'books': books})

def book_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.review_set.all()  # Retrieve all reviews for this book
    return render(request, 'crazy_book_clubs/book_reviews.html', {'book': book, 'reviews': reviews})

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crazy_book_clubs:book_list')
    else:
        form = BookForm()
    return render(request, 'crazy_book_clubs/new_book.html', {'form': form})

def new_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book  # Associate the review with the specific book
            review.save()
            return redirect('crazy_book_clubs:book_reviews', book_id=book.id)
        else:
            # If the form is not valid, render the form again with errors
            return render(request, 'crazy_book_clubs/new_review.html', {'form': form, 'book': book})
    else:
        form = ReviewForm()
        return render(request, 'crazy_book_clubs/new_review.html', {'form': form, 'book': book})


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('crazy_book_clubs:book_reviews', book_id=review.book.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'crazy_book_clubs/edit_review.html', {'form': form, 'review': review})

