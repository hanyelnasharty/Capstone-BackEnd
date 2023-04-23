from rest_framework import generics
from .serializers import RecommendationSerializer
from .models import Recommendation

class RecommendationList(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all().order_by('id')
    serializer_class = RecommendationSerializer

class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all().order_by('id')
    serializer_class = RecommendationSerializer
