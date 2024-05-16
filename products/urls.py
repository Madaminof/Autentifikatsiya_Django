from django.urls import path
from .views import BookDetailsView, BookListView, BookDeleteView, BookUptadeView, Savat, AddReview, ViewReview, \
    UptadeCommentView, ProfileView, ProfileUpdateView, Users,DeleteCommentView

app_name = 'products'
urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('detail/<int:pk>',BookDetailsView.as_view(), name='detail'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('book/update/<int:pk>/', BookUptadeView.as_view(), name='update'),
    path('Savat/<int:pk>', Savat.as_view(), name='savat'),
    path('review/<int:pk>', AddReview.as_view(), name='review'),
    path('view_review/<int:pk>',ViewReview.as_view(), name='view_review'),
    path('update_comment/<int:pk>', UptadeCommentView.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
    path('profile/', ProfileView.as_view(),name='profile'),
    path('profileupdate/', ProfileUpdateView.as_view(), name='profileupdate'),
    path('users', Users.as_view(),name='users')

]
