from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    
	department = models.CharField(max_length=200, null=True, blank=True)
	program_type = models.CharField(max_length=200, null=True, blank=True)
	country = models.CharField(max_length=200, null=True, blank=True)
	country_code = models.CharField(max_length=200, null=True, blank=True)

	university = models.CharField(max_length=200, null=True, blank=True)
	semester = models.CharField(max_length=200, null=True, blank=True)

	visa_type = models.CharField(max_length=200, null=True, blank=True)
	visa_issuance_time = models.CharField(max_length=200, null=True, blank=True)
	visa_issuance_procedure = models.CharField(max_length=200, null=True, blank=True)

	pre_departure_preparation = models.CharField(max_length=200, null=True, blank=True)
	dorm_register = models.CharField(max_length=200, null=True, blank=True)
	class_register = models.CharField(max_length=200, null=True, blank=True)
	pre_etc = models.CharField(max_length=200, null=True, blank=True)

	airport_to_campus_mobility = models.CharField(max_length=200, null=True, blank=True)
	airport_to_campus_time = models.CharField(max_length=200, null=True, blank=True)
	semester = models.CharField(max_length=200, null=True, blank=True)
	dorm_name = models.CharField(max_length=200, null=True, blank=True)
	dorm_cost = models.CharField(max_length=200, null=True, blank=True)
	dorm_address = models.CharField(max_length=200, null=True, blank=True)
	dorm_reputation = models.CharField(max_length=200, null=True, blank=True)
	dorm_website = models.CharField(max_length=200, null=True, blank=True)
	dorm_etc = models.CharField(max_length=200, null=True, blank=True)
	leisure = models.CharField(max_length=200, null=True, blank=True)
	staff_name = models.CharField(max_length=200, null=True, blank=True)
	staff_title = models.CharField(max_length=200, null=True, blank=True)
	staff_email = models.CharField(max_length=200, null=True, blank=True)
	is_consult = models.CharField(max_length=200, null=True, blank=True)
	support = models.CharField(max_length=200, null=True, blank=True)

	course_num = models.CharField(max_length=200, null=True, blank=True)
	course_name = models.CharField(max_length=200, null=True, blank=True)
	course_reputation = models.CharField(max_length=200, null=True, blank=True)
	course_procedure = models.CharField(max_length=200, null=True, blank=True)
	course_grading = models.CharField(max_length=200, null=True, blank=True)
	course_website = models.CharField(max_length=200, null=True, blank=True)
	course_etc = models.CharField(max_length=200, null=True, blank=True)

	flight = models.CharField(max_length=200, null=True, blank=True)
	pre_entry_preparation = models.CharField(max_length=200, null=True, blank=True)
	dorm_leaving = models.CharField(max_length=200, null=True, blank=True)
	program_end_procedure = models.CharField(max_length=200, null=True, blank=True)
	post_etc = models.CharField(max_length=200, null=True, blank=True)

	satisfaction = models.IntegerField(null=True, blank=True)
	impression = models.CharField(max_length=200, null=True, blank=True)
	suggestion = models.CharField(max_length=200, null=True, blank=True)

	introduction = models.TextField(null=True, blank=True)
	word_cloud_url = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.university

class Article(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	university = models.CharField(max_length=200, null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	recommand = models.IntegerField(null=True, blank=True)
	comment = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title