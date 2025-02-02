from django.db import models
from django.db.models.fields import FloatField

# Create your models here.
class Course(models.Model):
    course_id = models.TextField(primary_key=True)
    course_name = models.TextField()
    course_intro = models.TextField(blank=True, null=True)
    course_url = models.URLField()
    course_img_url = models.URLField(blank=True)
    course_price = models.IntegerField(blank=True)
    #max_price = models.IntegerField(blank=True, null=True)
    #min_price = models.IntegerField()
    #rating = models.FloatField()
    course_time = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teacher')
    website = models.ForeignKey('Website', on_delete=models.CASCADE, related_name='website')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='status')

    class Meta:
        db_table = 'COURSE"."course'

    def __str__(self) -> str:
        return self.course_name


class Teacher(models.Model):
    teacher_id = models.TextField(primary_key=True)
    teacher_name = models.TextField()
    teacher_img = models.URLField()
    teacher_introduction = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'COURSE"."teacher'
    
    def __str__(self) -> str:
        return self.teacher_id


class Website(models.Model):
    website_id = models.TextField(primary_key=True)
    website_name = models.TextField()
    website_url = models.URLField()

    class Meta:
        db_table = 'COURSE"."website'
    
    def __str__(self) -> str:
        return self.website_id


class Status(models.Model):
    status_id = models.TextField(primary_key=True)
    status_description = models.TextField()

    class Meta:
        db_table = 'COURSE"."status'
    
    def __str__(self) -> str:
        return self.status_description


class Fundraising(models.Model):
    fundraising_id = models.TextField(primary_key=True)
    fundraising_due_date = models.DateField()
    fundraising_process = FloatField(null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='fund_on_course')

    class Meta:
        db_table = 'COURSE"."fundraising'
    
    def __str__(self):
        return self.fundraising_id


class Discount(models.Model):
    discount_id = models.TextField(primary_key=True)
    discount_content = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='discount_on_course')

    class Meta:
        db_table = 'COURSE"."discount'

    def __str__(self):
        return self.discount_id


class StudentsCount(models.Model):
    students_count = models.IntegerField(),
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="students_of_course")
    update_date = models.DateTimeField()

    class Meta:
        db_table = 'COURSE"."students_count'
    
    def __str__(self):
        return f'{self.course}:{self.students_count}'


class Category(models.Model):
    category_id = models.TextField(primary_key=True)
    category_name = models.TextField()

    class Meta:
        db_table = 'COURSE"."category'
    
    def __str__(self):
        return self.category_name


class Review(models.Model):
    review_id = models.TextField(primary_key=True)
    review_content = models.TextField()
    review_star = models.IntegerField(null=True, blank=True)
    review_time = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="reviews_of_course")

    class Meta:
        db_table = 'COURSE"."review'
    
    def __str__(self):
        return self.review_content