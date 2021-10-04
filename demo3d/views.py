import os
import time
from django.db.models import Q
from datetime import date
import json
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile

from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import default_storage

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail

from theta_image.models import ThetaImage


def home_view(request):
	images = ThetaImage.objects

	args = {
		'images': images
	}
	return render(request, 'index.html', args)


def details(request, pk):
	images = ThetaImage.objects
	image = get_object_or_404(ThetaImage, pk=pk)

	args = {
		'image': image,
		'images': images
	}
	return render(request, 'details.html', args)