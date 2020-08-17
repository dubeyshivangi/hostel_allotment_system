from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Student

def student_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='students')
		instance.groups.add(group)
		Student.objects.create(
			user=instance,
			student_name=instance.username,
            student_mail=instance.email,
			)
		print('Profile created!')

post_save.connect(student_profile, sender=User)
