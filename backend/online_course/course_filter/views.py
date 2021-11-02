from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course_filter.models import Course, Teacher, Website, Status, Fundraising, Discount, StudentsCount

from django.db.models import Count
from django.db.models import Q
import datetime

# Create your views here.
@api_view(['POST'])
def quick_search(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        try:
            content = request.data['Input']
        except KeyError:
            return Response("4 parameters are all required.(StartStation,EndStation,OutWardSearchDate,OutWardSearchTime)", status=status.HTTP_400_BAD_REQUEST)

        potentioal_tid = Teacher.objects.filter(teacher_name__icontains=content).values('teacher_id')
        potential_course = list(Course.objects.filter(
            Q(course_name__contains=content) |
            Q(teacher_id__in=potentioal_tid) |
            Q(course_description__contains=content)).values())

        result = []
        for i in range(len(potentioal_course)):
            data = {}
            data['course_name'] = potential_course[i]['course_name']
            data['course_description'] = potential_course[i]['course_description']
            data['course_img'] = potential_course[i]['course_img']
            data['total_length'] = potential_course[i]['length']
            data['min_price'] = potential_course[i]['min_price']
            data['max_price'] = potential_course[i]['max_price']
            
            status = Status.objects.filter(status_id = potential_course[i]['status_id']).values('status_name')[0]['status_name']
            data['status'] = status
            teacher_name = Teacher.objects.filter(teacher_id = potential_course[i]['teacher_id']).values('teacher_name')[0]['teacher_name']
            data['teacher_name'] = teacher_name
            students_count = StudentsCount.objects.filter(course_id = potential_course[i]['course_id']).values('students_count')[0]['students_count']
            data['students_count'] = students_count
            website_name = Website.objects.filter(website_id = potential_course[i]['website_id']).values('website_name')[0]['website_name']
            data['website_name'] = website_name

            result.append(data)
    
        return Response(result, status=status.HTTP_200_OK)