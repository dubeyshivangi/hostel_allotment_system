from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profilepic.png", null=True, blank=True)
    # fee_receipt=models.FileField(default='')
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    student_name = models.CharField(max_length=200, null=True)
    student_mail = models.CharField(max_length=200, null=True)
    student_contact=models.CharField(max_length=10, null=True)
    father_name = models.CharField(max_length=200, null=True)
    enrollment_no = models.IntegerField(unique=True, null=True)
    courses = (
        ('BTECH','BTECH'),
        ('MCA','MCA'),
        ('MBA','MBA'),
        ('MTECH','MTECH'),
    )
    course = models.CharField(max_length=50,null=True,choices=courses)
    student_address=models.CharField(max_length=200,null=True)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    YEARS_CHOICE = (
        ('First','First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Fourth','Fourth'),
    )

    curr_year = models.CharField(max_length=50,null=True,choices=YEARS_CHOICE)
    fees_receipt=models.FileField(null=True,blank=True)
    room = models.IntegerField(null=True)
    room_allotted = models.BooleanField(default=False)
    no_dues = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name


class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('T', 'Triple Occupancy')]
    floors = (
        ('First','First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Fourth','Fourth'),
    )
    floor = models.CharField(max_length=50,null=True,choices=floors)
    no = models.CharField(max_length=5)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None) 
    capacity = models.IntegerField(default=None)  
    # vacant = models.BooleanField(default=False)

    def Claimroom(self):
        # print('work1')
        if self.capacity>1:
            # print('work2')
            self.capacity=self.capacity-1
            self.save()

    def __str__(self):
        return self.no

class Notice(models.Model):
    notice=models.FileField()
    title=models.CharField(max_length=100,null=True)

# class Hostel(models.Model):
#     name = models.CharField(max_length=5)
#     gender_choices = [('M', 'Male'), ('F', 'Female')]
#     gender = models.CharField(
#         choices=gender_choices,
#         max_length=1,
#         default=None,
#         null=True)
#     # course = models.ManyToManyField('Course', default=None, blank=True)
#     # warden_name = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.name


# class Course(models.Model):
#     course = models.CharField(max_length=100, null=True)
  
#     def __str__(self):
#         return self.course


# class Warden(models.Model):
#     user = models.OneToOneField(
#         User,
#         default=None,
#         null=True,
#         on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     hostel = models.ForeignKey('Hostel',
#         default=None,
#         null=True,
#         on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name