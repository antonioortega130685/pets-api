from rest_framework.serializers import ModelSerializer

from dc3.models import Pet



class PetCreateUpdateSerializer(ModelSerializer):
	class Meta: 
		model = Pet
		fields = [
		    'species',
		    'name',
		    'birthday',
		]


class PetDetailSerializer(ModelSerializer):
	class Meta: 
		model = Pet
		fields = [
		    'species',
		    'name',
		    'birthday',
		    'owner'
		]

class PetListSerializer(ModelSerializer):
	class Meta: 
		model = Pet
		fields = [
		    'name',
		    'owner'
		]

