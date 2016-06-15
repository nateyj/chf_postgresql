from .. import dmp_render, dmp_render_to_string	# relative import notation for the next line
# from homepage import dmp_render, dmp_render_to_string
from datetime import datetime
from django.conf import settings
from django_mako_plus import view_function
import random

@view_function
def process_request(request):
	context = {
		'now': datetime.now().strftime(request.urlparams[0] or '%H:%M'),
		'timecolor': random.choice(['red', 'blue', 'green', 'brown']),
	}

	return dmp_render(request, 'index.html', context)