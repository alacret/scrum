from django.forms import ModelForm, PasswordInput
from comercio.models import Publicacion, Comerciante

# Create the form class.
class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion

class ComercianteForm(ModelForm):
	# password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Comerciante
		widgets = {
			'password':PasswordInput()
		}