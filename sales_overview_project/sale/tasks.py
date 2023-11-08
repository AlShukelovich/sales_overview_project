import json
from django.forms import model_to_dict
from sale.models import Sale

from sales_overview_project.celery import app

@app.task
def create_file_json():
    with open(f"sales_list.json", "w+") as new_file:
        dict_from_db = [model_to_dict(todo) for todo in Sale.objects.all()]
        json.dump(str(dict_from_db), new_file)