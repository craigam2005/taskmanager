from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

PRIORITY_CHOICES= (
    (1,'low'),
    (2,'medium'),
    (3,'high'),
)


class Task(models.Model):
    
    title = models.CharField('discription', max_length=250, null=False)
    priority = models.BigIntegerField('priority',choices=PRIORITY_CHOICES, default=2, null=False)
    guts_ticket = models.URLField('Guts Ticket', unique=True,null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date= models.DateField('due date')
    done = models.BooleanField(default= False)
    
    #guts_t = models.URLField.__str__("www.google.com"+guts_ticket, null=True)
    def __unicode__(self):
        return smart_unicode(self.title)