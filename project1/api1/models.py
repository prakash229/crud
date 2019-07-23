from django.db import models

class todolist(models.Model):
    datebegan=models.DateTimeField(auto_now=False, auto_now_add=True)
    taskdetails=models.CharField(max_length=255)
    taskstatus=models.BooleanField(default=False)

    def __str__(self):
        return "{} * {} * {}".format(self.datebegan,self.taskdetails,self.taskstatus)
