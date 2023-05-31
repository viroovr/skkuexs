from django.shortcuts import render
from django.utils import timezone
from .models import Report, Article
import requests
import json

# import openai

def main(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })

	rank = sum(report.rank for report in report_list) // len(report_list)

	# openai.api_key = "api키 입력" # api키 발급 링크: https://platform.openai.com/account/api-keys
	# introduction = ""
	# try:
	# 	completion = openai.ChatCompletion.create(
	# 		model="gpt-3.5-turbo",
	# 		messages=[{"role": "user", "content": school_name+"의 위치와 특징을 한글로 한 줄로 말해줘"}]     
	# 	)
	# 	introduction = completion.choices[0].message.content
	# except:
	# 	introduction = "api 호출 실패"

	context = {
		'school_name': school_name,
		'rank': rank,
		# 'introduction': introduction
		'introduction': 'Nulla Lorem mollit cupidatat irure. Laborum' #api 사용 시 윗줄을 대신 이용
	}

	return render(request, 'forums/main.html', context)

def submain_preparation(request, school_name):
	return render(request, 'forums/submain_preparation.html', { 'school_name': school_name })

def submain_uni_life(request, school_name):
	return render(request, 'forums/submain_uni_life.html', { 'school_name': school_name })

def courses(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)

	course_name = []
	courses = []
	for report in report_list:
		course_name.append(report.course_name)
		courses.append({'rank': report.rank,
		  				'title': report.course_num,
						'date': report.user_duration,
						'content': report.course_etc
						})
	context = {
        'school_name': school_name,
        'course_name': course_name,
        'courses': courses
	}
	return render(request, 'forums/courses.html', context)

def uni_review(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)

	uni_review = []
	for report in report_list:
		uni_review.append({ 'rank': report.rank,
							'date': report.user_duration,
							'photo': ['/static/images/Harvard2.jpg'],
							'photo_num': 1,
							'content': report.etc_feel
							})
	context = {
		'school_name': school_name,
		'uni_review': uni_review
	}
	return render(request, 'forums/uni_review.html', context)

def community(request, school_name):
	article_list = Article.objects.filter(user_university=school_name)

	community = []
	for article in article_list:
		community.append({ 'title': article.title,
							'content': article.content,
							'date': article.date.date,
							'recommand': article.recommand,
							'comment': article.comment
							})
	context = {
		'school_name': school_name,
		'community': community
	}
	return render(request, 'forums/community.html', context)

def visa(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	report = report_list[0]
	context = {
        'school_name': school_name,
        'visa_type': report.pre_visa_type,
        'visa_period': report.pre_visa_apply_duration,
        'visa_application_process': [
			report.pre_visa_how,
			report.pre_visa_ready_check
        ],
        'update_date': str(timezone.now())
    }
	return render(request, 'forums/visa.html', context)

def dorm(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	report = report_list[0]
	context = {
        'school_name': school_name,
		'dorm_list': [report.now_dorm_name for report in report_list],
		'dorm_cost': report.now_cost,
		'dorm_link': report.now_website,
		'dorm_characteristics': report.now_etc,
        'update_date': str(timezone.now())
    }
	return render(request, 'forums/dorm.html', context)

def etc_pre(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	context = {
        'school_name': school_name,
		'pre_list': [report.pre_etc for report in report_list],
		'pre_info': [report.pre_etc for report in report_list]
    }
	return render(request,'forums/etc_pre.html', context)