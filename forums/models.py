from django.db import models

class Report(models.Model):
    
	user_department = models.CharField(max_length=200, null=True, blank=True)
	user_type = models.CharField(max_length=200, null=True, blank=True)
	user_country = models.CharField(max_length=200, null=True, blank=True)
	user_country_code = models.CharField(max_length=200, null=True, blank=True)

	user_university = models.CharField(max_length=200, null=True, blank=True)
	user_duration = models.CharField(max_length=200, null=True, blank=True)

	pre_visa_type = models.CharField(max_length=200, null=True, blank=True)
	pre_visa_apply_duration = models.CharField(max_length=200, null=True, blank=True)
	pre_visa_how = models.CharField(max_length=200, null=True, blank=True)
	pre_visa_ready_check = models.CharField(max_length=200, null=True, blank=True)
	pre_dorm_register = models.CharField(max_length=200, null=True, blank=True)
	pre_class_register = models.CharField(max_length=200, null=True, blank=True)
	pre_etc = models.CharField(max_length=200, null=True, blank=True)

	now_move_how = models.CharField(max_length=200, null=True, blank=True)
	now_move_time = models.CharField(max_length=200, null=True, blank=True)
	now_semester = models.CharField(max_length=200, null=True, blank=True)
	now_dorm_name = models.CharField(max_length=200, null=True, blank=True)
	now_cost = models.CharField(max_length=200, null=True, blank=True)
	now_dorm_address = models.CharField(max_length=200, null=True, blank=True)
	now_reputation = models.CharField(max_length=200, null=True, blank=True)
	now_website = models.CharField(max_length=200, null=True, blank=True)
	now_etc = models.CharField(max_length=200, null=True, blank=True)
	now_leisure = models.CharField(max_length=200, null=True, blank=True)
	now_staff_name = models.CharField(max_length=200, null=True, blank=True)
	now_staff_position = models.CharField(max_length=200, null=True, blank=True)
	now_staff_email = models.CharField(max_length=200, null=True, blank=True)
	now_is_consult = models.CharField(max_length=200, null=True, blank=True)
	now_support = models.CharField(max_length=200, null=True, blank=True)

	course_num = models.CharField(max_length=200, null=True, blank=True)
	course_name = models.CharField(max_length=200, null=True, blank=True)
	course_reputation = models.CharField(max_length=200, null=True, blank=True)
	course_how = models.CharField(max_length=200, null=True, blank=True)
	course_grading = models.CharField(max_length=200, null=True, blank=True)
	course_website = models.CharField(max_length=200, null=True, blank=True)
	course_etc = models.CharField(max_length=200, null=True, blank=True)

	post_flight = models.CharField(max_length=200, null=True, blank=True)
	post_ready_check = models.CharField(max_length=200, null=True, blank=True)
	post_dorm_end = models.CharField(max_length=200, null=True, blank=True)
	post_how_end = models.CharField(max_length=200, null=True, blank=True)
	post_etc = models.CharField(max_length=200, null=True, blank=True)

	# etc_good = models.CharField(max_length=200, null=True, blank=True)
	etc_feel = models.CharField(max_length=200, null=True, blank=True)
	ect_say = models.CharField(max_length=200, null=True, blank=True)

	rank = models.IntegerField()
	introduction = models.TextField(null=True, blank=True)
	wordCloudUrl = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.user_university

class Article(models.Model):
	user_university = models.CharField(max_length=200, null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	recommand = models.IntegerField()
	comment = models.IntegerField()