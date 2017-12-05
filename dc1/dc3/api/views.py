from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView, 
	UpdateAPIView, 
	RetrieveUpdateAPIView
	)

from .serializers import (
	PetCreateUpdateSerializer,
	PetDetailSerializer,
	PetListSerializer
	)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

	)

from .permissions import IsOwnerOrReadOnly


from dc3.models import Pet


class PetCreateAPIView(CreateAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PetDeleteAPIView(DestroyAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]


class PetDetailAPIView(RetrieveAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]


class PetListAPIView(ListAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetListSerializer

class PetUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetCreateUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



