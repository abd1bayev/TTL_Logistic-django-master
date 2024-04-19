from django.urls import path

from projects.views import ContactInformationView, \
    SearchResultsView, ReviewListAPIView
from projects.views.about import AboutListView
from projects.views.contact import ContactAPIView
from projects.views.news import NewsListAPIView, NewsRetrieveView
from projects.views.service import ServiceListAPIView, ServiceRetrieveView

urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('news/', NewsListAPIView.as_view(), name='news-list-create'),
    path('news/<str:slug>/', NewsRetrieveView.as_view(), name='news-retrieve-update-destroy'),

    path('about/', AboutListView.as_view(), name='about-list'),
    path('news/', NewsListAPIView.as_view(),
         name='news-list-create'),
    path('news/<str:slug>/', NewsRetrieveView.as_view(),
         name='news-retrieve-update-destroy'),

    path('contact-information/', ContactInformationView.as_view(), name='contact-information'),

    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceRetrieveView.as_view(), name='service-retrieve'),

    path('contact/', ContactAPIView.as_view(), name='contact-list-create'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('reviews/', ReviewListAPIView.as_view(), name="reviews"),
]
