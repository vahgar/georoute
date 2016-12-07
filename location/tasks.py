from celery.decorators import task
from celery.utils.log import get_task_logger
from location.models import Location

@task(name="del")
def delete_loc():
    obj = Location.objects.get(id=9)
    obj.delete
