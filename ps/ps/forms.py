from django.forms import ModelForm
from comercio.models import Publicacion

# Create the form class.
class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion
