from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Team(models.Model):
    name = models.CharField(_("Team Name"), max_length=50)
    description = models.TextField(_("About Team"))
    owner = models.ForeignKey(CustomUser, verbose_name=_("Team Owner"),related_name='team_owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, verbose_name=_("Team Members"),related_name='team_member',blank=True)

    def __str__(self) :
        return self.name
    