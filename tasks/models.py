from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
from teams.models import Team
# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=255,blank=False , null=False )
    description = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(_("Created at"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_done = models.BooleanField(_("Is Done") ,default=False)
    team = models.ForeignKey(Team, verbose_name=_("Team Name"), on_delete=models.CASCADE , blank=True, null=True)
    def __str__(self) :
        return self.title