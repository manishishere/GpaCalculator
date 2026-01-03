from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Details(models.Model):
    GRADE_CHOICE = [
        ('A', 'A (4.0)'),
        ('A-', 'A- (3.7)'),
        ('B+', 'B+ (3.3)'),
        ('B', 'B (3.0)'),
        ('B-', 'B- (2.7)'),
        ('C+', 'C+ (2.3)'),
        ('C', 'C (2.0)'),
        ('C-', 'C- (1.7)'),
        ('D+', 'D+ (1.3)'),
        ('D', 'D (1.0)'),
        ('F', 'F (0.0)'),

    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    s_name = models.CharField(max_length=150, null=False, blank=False)
    s_grade = models.CharField(max_length=150, choices=GRADE_CHOICE, null=False, blank=True)
    s_credit = models.IntegerField(null=False, blank= False,validators=[MinValueValidator(0.5), MaxValueValidator(6)])











































































# # Create your models here.
# class Student(models.Model):
#     LEVEL_CHOICES  = [
#         ('UG', 'Undergraduate'),
#         ('G', 'Graduate'),
#     ] 
#     COURSE_CHOICES = [
#         ('BESE', 'BE Software Engineering'),
#         ('BEIT', 'BE Information Technology'),
#         ('BECE', 'BE Computer Engineering'),
#         ('BECIVIL', 'BE Civil Engineering'),
#         ('MSCCS', 'MSc Computer Science'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     course_name = models.CharField(max_length=150,choices=COURSE_CHOICES, null=False,blank=False)
#     course_level = models.CharField(max_length=2,choices=LEVEL_CHOICES, null=False,
#     blank=False)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     current_semester = models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(8)],
#         default=1)
#     def __str__(self):
#         return self.course_name
#     class Meta: #order_by rakhyo bhane sadhai rakhna paryo tara meta ma ekchoti matra rakhe pugcha
#         ordering = ['-created_at']




# class Course(models.Model):
#     """Model for academic courses"""
#     LEVEL_CHOICES = [
#         ('UG', 'Undergraduate'),
#         ('G', 'Graduate'),
#     ]
    
#     course_code = models.CharField(max_length=20, unique=True)
#     course_name = models.CharField(max_length=200)
#     course_level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
#     total_semesters = models.IntegerField(default=8)
    
#     class Meta:
#         ordering = ['level', 'name']
    
#     def __str__(self):
#         return f"{self.code} - {self.name}"





# class Subject(models.Model):
#     """Model for subjects in each course"""
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
#     semester = models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(8)]
#     )
#     subject_code = models.CharField(max_length=20)
#     subject_name = models.CharField(max_length=200)
#     credit_hours = models.FloatField(
#         validators=[MinValueValidator(0.5), MaxValueValidator(6)]
#     )
    
#     class Meta:
#         ordering = ['course', 'semester', 'code']
#         unique_together = ['course', 'semester', 'code']
    
#     def __str__(self):
#         return f"{self.code} - {self.name}"





