from django.forms import ModelForm

# Create the form class.
class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion
