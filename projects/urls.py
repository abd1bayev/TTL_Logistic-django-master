from django.urls import path
from projects.views.reviews import ReviewCreateAPIView

from projects.views.about import AboutListView
from projects.views.contact import ContactInformationView
from projects.views.blog import BlogListAPIView, BlogRetrieveView
from projects.views.service import ServiceListAPIView, ServiceRetrieveView

urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('blog/', BlogListAPIView.as_view(), name='blog-list-create'),
    path('blog/<str:slug>/', BlogRetrieveView.as_view(), name='blog-retrieve-update-destroy'),

    path('about/', AboutListView.as_view(), name='about-list'),
    path('blog/', BlogListAPIView.as_view(),
         name='blog-list-create'),
    path('blog/<str:slug>/', BlogRetrieveView.as_view(),
         name='blog-retrieve-update-destroy'),

    path('contact-information/', ContactInformationView.as_view(), name='contact-information'),

    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceRetrieveView.as_view(), name='service-retrieve'),

    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review_create'),

]
