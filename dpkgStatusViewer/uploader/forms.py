from django import forms
from s3direct.widgets import S3DirectWidget

class UploadFileForm(forms.Form):
    status = forms.URLField(widget=S3DirectWidget(dest='primary_destination'))