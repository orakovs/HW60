from django.urls import path
from .views import *

urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='organization_list'),
    path('organization/<int:pk>', OrganizationDetailView.as_view(), name='organization_detail'),
    path('create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('delete/<int:pk>', OrganizationDeleteView.as_view(), name='organization_delete'),
    path('update/<int:pk>', OrganizationUpdateView.as_view(), name='organization_update')
]