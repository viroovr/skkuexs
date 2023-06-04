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

	report = report_list[0]
	context = {
		'school_name': school_name,
		'rank': sum(report.rank for report in report_list) // len(report_list),
		'introduction': report.introduction,
		'wordCloudUrl':report.wordCloudUrl,
		'country': report.user_country
	}

	return render(request, 'forums/main.html', context)

def submain_preparation(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	context = {
		'school_name': school_name,
		'country': report_list[0].user_country if report_list else 'South Korea'
	}
	return render(request, 'forums/submain_preparation.html', context)

def submain_uni_life(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	context = {
		'school_name': school_name,
		'country': report_list[0].user_country if report_list else 'South Korea'
	}
	return render(request, 'forums/submain_uni_life.html', context)

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
        'courses': courses,
		'country': report_list[0].user_country if report_list else 'South Korea'
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
		'uni_review': uni_review,
		'country': report_list[0].user_country if report_list else 'South Korea'
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
	report_list = Report.objects.filter(user_university=school_name)
	context = {
		'school_name': school_name,
		'community': community,
		'country': report_list[0].user_country if report_list else 'South Korea'
	}
	return render(request, 'forums/community.html', context)

def visa(request, school_name):
	report_list = Report.objects.filter(user_university=school_name)
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	update_date = Report.objects.filter(user_university=school_name).exclude(pre_visa_how__exact='').aggregate(Max('user_duration'))
	report = report_list[0]
	context = {
        'school_name': school_name,
        'visa_type': report.pre_visa_type,
        'visa_period': report.pre_visa_apply_duration,
        'visa_application_process': [
			report.pre_visa_how,
			report.pre_visa_ready_check
        ],
		'country': report.user_country,
		'country_code': report.user_country_code,
        'update_date': update_date
    }
	return render(request, 'forums/visa.html', context)

from django.db.models import Count

def dorm(request, school_name):
	report_list = Report.objects.filter(user_university=school_name).annotate(count_now_dorm_name=Count('now_dorm_name',distinct=True)).order_by('-count_now_dorm_name')[:5]

	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	webSite = Report.objects.filter(user_university=school_name).exclude(now_website__exact='').filter(now_website__startswith='http')
	if(webSite):
		webSite = webSite[0].now_website
	else:
		webSite = ""
	
	update_date = Report.objects.filter(user_university=school_name).exclude(now_etc__exact='').aggregate(Max('user_duration'))
	report = report_list[0]

	def name_filter(x):
		if(x):
			if(x == '-'):
				pass
			else:
				return x
		else:
			pass

	context = {
        'school_name': school_name,
		'dorm_list': list(set(list(filter(name_filter, [report.now_dorm_name.strip() for report in report_list])))),
		'dorm_cost': max([report.now_cost for report in report_list],key=len),
		'dorm_link': webSite,
		'dorm_characteristics': report.now_etc,
        'update_date': update_date,
		'country': report.user_country
    }
	return render(request, 'forums/dorm.html', context)

def etc_pre(request, school_name):
	report_list = Report.objects.filter(user_university=school_name).exclude(pre_etc__exact='').order_by('-user_duration')
	if not report_list:
		return render(request, 'forums/empty.html', { 'school_name': school_name })
	
	update_date = Report.objects.filter(user_university=school_name).exclude(pre_etc__exact='').aggregate(Max('user_duration'))
	report = report_list[0]
	context = {
        'school_name': school_name,
		'pre_list': [],
		'pre_info': [{
				'content': report.pre_etc,
				'date': report.user_duration,
			}
			for report in report_list],
		'update_date': update_date,
		'country': report.user_country
    }
	return render(request,'forums/etc_pre.html', context)
