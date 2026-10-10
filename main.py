import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule_manager.settings")
django.setup()

from logic.models import Subject, Teacher

subject1 = Subject(name="Mathematics", description="Study of numbers, quantities, and shapes.")
teacher1 = Teacher(first_name="Stepan", last_name="Giga", email="giga@gmail.com", subject=subject1)

subject1.save()
teacher1.save()
