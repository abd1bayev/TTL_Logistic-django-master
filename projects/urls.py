from django.urls import path

from projects.views import TeamMemberDetailView, TeamMemberListView, ContactInformationView, PartnerView, \
    SearchResultsView, ReviewListAPIView
from projects.views.about import AboutListView
from projects.views.contact import ContactAPIView
from projects.views.news import NewsListAPIView, NewsRetrieveView
from projects.views.publications import PublicationListAPIView, PublicationRetrieveView
from projects.views.service import ServiceListAPIView, ServiceRetrieveView

urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('news/', NewsListAPIView.as_view(), name='news-list-create'),
    path('news/<str:slug>/', NewsRetrieveView.as_view(), name='news-retrieve-update-destroy'),
    path('team-member/', TeamMemberListView.as_view(), name='team-member-list'),
    path('team-member/<str:slug>/', TeamMemberDetailView.as_view(), name='team-member-detail'),
    path('about/', AboutListView.as_view(), name='about-list'),
    path('news/', NewsListAPIView.as_view(),
         name='news-list-create'),
    path('news/<str:slug>/', NewsRetrieveView.as_view(),
         name='news-retrieve-update-destroy'),
    path('publications/', PublicationListAPIView.as_view(),
         name='publication-list-create'
         ),
    path('publications/<str:slug>/', PublicationRetrieveView.as_view(),
         name='publication-retrieve'
         ),

    path('contact-information/', ContactInformationView.as_view(), name='contact-information'),

    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceRetrieveView.as_view(), name='service-retrieve'),

    path('contact/', ContactAPIView.as_view(), name='contact-list-create'),
    path('partners/', PartnerView.as_view(), name='partners'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('reviews/', ReviewListAPIView.as_view(), name="reviews"),
]
