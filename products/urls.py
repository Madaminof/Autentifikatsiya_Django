from django.urls import path
from .views import BookDetailView, BookListView, BookDeleteView, BookUptadeView, Savat, AddReview, ViewReview

app_name = 'products'
urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('book/update/<int:pk>/', BookUptadeView.as_view(), name='update'),
    path('Savat/<int:pk>', Savat.as_view(), name='savat'),
    path('review/<int:pk>', AddReview.as_view(), name='review'),
    path('view_review/<int:pk>',ViewReview.as_view(), name='view_review')
]
