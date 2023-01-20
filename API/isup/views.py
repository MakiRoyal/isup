from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions
from isup.models import Domain
from isup.serializers import DomainSerializer


class HomingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all().order_by("id")
    serializer_class = DomainSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"
