from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy



class OrganizationListView(ListView):
    model = Organization
    template_name = 'organizations.html'
    context_object_name = 'Organizations'


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'organization.html'
    context_object_name = 'Organization'


class OrganizationCreateView(CreateView):
    model = Organization
    template_name = 'create_organization.html'
    fields = ['name', 'legal_form']
    success_url = reverse_lazy('organization_list')


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'delete_organization.html'
    success_url = reverse_lazy('organization_list')


class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = 'update_organization.html'
    fields = ['name', 'legal_form']
    success_url = reverse_lazy('organization_list')
