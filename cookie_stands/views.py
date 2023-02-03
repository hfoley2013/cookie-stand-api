from django.shortcuts import render, redirect
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer
from .forms import CookieStandForm


class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


def create_cookie_stand(request):
    if request.method == 'POST':
        form = CookieStandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cookie_stands')
    else:
        form = CookieStandForm()
    return render(request, 'create_cookie_stand.html', {'form': form})
