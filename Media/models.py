from django.db import models
from django.contrib.auth.models import User
from workflow.models import States
import os, uuid
from django.conf import settings

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	if ext == 'mp3' or ext == 'wav' or ext == 'ogg' :
		return os.path.join('audio', filename)
	if ext == 'jpg' or ext == 'jpeg' or ext == 'png':
		return os.path.join('images', filename)
	if ext == 'vob' or ext == 'webm' or ext == 'avi' or ext == 'mp4' or ext == 'wmv':
		return os.path.join('video', filename)

class Media(models.Model):
	media_types = (
		('IMAGE', 'Image'),
        ('AUDIO', 'Audio'),
        ('VIDEO', 'Video'),
    )
	mediatype = models.CharField(choices=media_types, max_length=10, default='IMAGE')	
	title = models.CharField(max_length=100)
	mediafile = models.FileField(null=True,upload_to=get_file_path)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,null=True,related_name='media_author')
	published_on=models.DateTimeField(null=True)
	published_by=models.ForeignKey(User,null=True,related_name='media_publisher')
	views = models.PositiveIntegerField(default=0)
	state = models.ForeignKey(States, null=True,related_name='media_workflow')