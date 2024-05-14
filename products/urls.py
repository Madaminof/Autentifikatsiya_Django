from django.urls import path
from .views import BookDetailView, BookListView, BookDeleteView, BookUptadeView, Savat, AddReview, ViewReview,UptadeCommentView

app_name = 'products'
urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('book/update/<int:pk>/', BookUptadeView.as_view(), name='update'),
    path('Savat/<int:pk>', Savat.as_view(), name='savat'),
    path('review/<int:pk>', AddReview.as_view(), name='review'),
    path('view_review/<int:pk>',ViewReview.as_view(), name='view_review'),
   # path('delete_review/<int:pk>', delete_comment, name='delete_review'),

   path('update_comment/<int:pk>', UptadeCommentView.as_view(), name='update_comment')

]
