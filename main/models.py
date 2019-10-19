from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.utils.translation import ugettext as translate
from django.utils.timezone import now
from main.file_format import ContentTypeRestrictedFileField
import datetime

class AutoCreatedUpdatedMixin(models.Model):

	created_at = models.DateTimeField(
		verbose_name=translate('created at'),
		unique=False,
		null=True,
		blank=True,
		db_index=True,
	)

	updated_at = models.DateTimeField(
		verbose_name=translate('updated at'),
		unique=False,
		null=True,
		blank=True,
		db_index=True,
	)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if not self.created_at:
			self.created_at = now()
			self.updated_at = self.created_at
		else:
			auto_updated_at_is_disabled = kwargs.pop('disable_auto_updated_at', False)
			if not auto_updated_at_is_disabled:
				self.updated_at = now()
		super(AutoCreatedUpdatedMixin, self).save(*args, **kwargs)


class SoftDeleteMixin(models.Model):

	deleted_at = models.DateTimeField(
		verbose_name=translate('deleted at'),
		unique=False,
		null=True,
		blank=True,
		db_index=True,
	)

	class Meta:
		abstract = True

	def delete(self, using=None, keep_parents=False):
		self.deleted_at = now()
		kwargs = {
			'using': using,
		}
		if hasattr(self, 'updated_at'):
			kwargs['disable_auto_updated_at'] = True
		self.save(**kwargs)

class Department(AutoCreatedUpdatedMixin,SoftDeleteMixin):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Course(AutoCreatedUpdatedMixin,SoftDeleteMixin):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department,on_delete=models.CASCADE)

	def __str__(self):
		return self.name + ", " + self.department.name

	def as_dict(self):
		return {
			"name":self.name,
			"id":self.id
		}


class User(AbstractUser,AutoCreatedUpdatedMixin,SoftDeleteMixin):
	is_student = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_department = models.BooleanField(default=False)
	is_club = models.BooleanField(default=False)
	department = models.ForeignKey(Department,on_delete=models.CASCADE , related_name='dept',blank=True, null=True)
	contact = models.CharField(max_length=20, default=False)
	contri = models.IntegerField(default=0)
	

	# def save(self, *args, **kwargs):
	# 	super(User, self).save(*args, **kwargs)
	# 	self.t_id = "T19"+str(12000+int(self.id)) 
	# 	super(User, self).save(*args, **kwargs)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Book(AbstractUser,AutoCreatedUpdatedMixin,SoftDeleteMixin):
	user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='book')
	document = ContentTypeRestrictedFileField(upload_to='static/books/', content_types=['application/docx', 'application/pdf', 'application/doc', 'application/odt', ],max_upload_size=5242880,blank=True, null=True)
	author = models.CharField(max_length=100, blank=False)
	title = models.CharField(max_length=100, blank=False)
	is_approved = models.BooleanField(default=False)

class Note(AbstractUser,AutoCreatedUpdatedMixin,SoftDeleteMixin):
	user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='note')
	document = ContentTypeRestrictedFileField(upload_to='static/notes/', content_types=['application/docx', 'application/pdf', 'application/doc', 'application/odt', ],max_upload_size=5242880,blank=True, null=True)
	course = models.ForeignKey(Course,on_delete=models.CASCADE , related_name='nc')
	title = models.CharField(max_length=100, blank=False)
	is_approved = models.BooleanField(default=False)

class MiscNote(AbstractUser,AutoCreatedUpdatedMixin,SoftDeleteMixin):
	user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='mis')
	document = ContentTypeRestrictedFileField(upload_to='static/misc/', content_types=['application/docx', 'application/pdf', 'application/doc', 'application/odt', ],max_upload_size=5242880,blank=True, null=True)
	desc = models.CharField(max_length=100, blank=False)
	title = models.CharField(max_length=100, blank=False)
	is_approved = models.BooleanField(default=False)

class CourseVideo(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='video')
	course = models.ForeignKey(Course,on_delete=models.CASCADE , related_name='vc')
	name= models.CharField(max_length=500)
	videofile= models.FileField(upload_to='static/videos/', null=True, verbose_name="")

	def __str__(self):
		return self.name + ": " + str(self.videofile)




