from django.shortcuts import render
from django.utils import timezone
from .models import Report, Article
import requests
import json
from django.db.models import Max


def main(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })

	rank = sum(report.rank for report in report_list) // len(report_list)
	introduction = report_list[0].introduction
	wordCloudUrl = "" # 여기에 url 정보 가져오기. 데이터 없으면 그냥 공백이어도 됨

	context = {
		'school_name': school_name,
		'rank': rank,
		'introduction': introduction,
		'wordCloudUrl' : wordCloudUrl,
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

	country = "South Korea" # 예시: Denmark, 값이 없을 리는 없는데 혹시 없으면 'South Korea'
	country_code = "kr" # 예시: dk, 이것도 값이 없을 리 없는데 없으면 'kr'

	context = {
        'school_name': school_name,
        'visa_type': report.pre_visa_type,
        'visa_period': report.pre_visa_apply_duration,
        'visa_application_process': [
			report.pre_visa_how,
			report.pre_visa_ready_check
        ],
		'country': country,
		'country_code': country_code,
        'update_date': str(timezone.now())
    }
	return render(request, 'forums/visa.html', context)

def dorm(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	webSite = Report.objects.filter(user_university=school_name).exclude(now_website__exact='').filter(now_website__startswith='http')[0].now_website
	
	report = report_list[0]
	context = {
        'school_name': school_name,
		'dorm_list': list(set(list(filter(None, [report.now_dorm_name.strip() for report in report_list])))),
		'dorm_cost': report.now_cost,
		'dorm_link': webSite,
		'dorm_characteristics': report.now_etc,
        'update_date': str(timezone.now())
    }
	return render(request, 'forums/dorm.html', context)



def etc_pre(request, school_name):
	report_list = Report.objects.filter(user_university=school_name).exclude(pre_etc__exact='').order_by('-user_duration')
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	update_date = Report.objects.filter(user_university=school_name).aggregate(Max('user_duration'))

	context = {
        'school_name': school_name,
		'pre_list': [],
		'pre_info': [{
				'content': report.pre_etc,
				'date': report.user_duration,
			}
			for report in report_list],
		'update_date': update_date
    }
	return render(request,'forums/etc_pre.html', context)