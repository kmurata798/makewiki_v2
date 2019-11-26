from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer
# from api.serializers import ChoiceSerializer

class Page_list(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class Page_detail(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
