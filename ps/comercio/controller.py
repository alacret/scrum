from ps.forms import PublicacionForm, ComercianteForm
from comercio.models import Publicacion

def save_pub(post):
	form = PublicacionForm(post)
	if form.is_valid():
		return form.save()
	return None
