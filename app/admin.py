from django.contrib import admin

from django.db import models 
from django.forms import CheckboxSelectMultiple

from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import *

def add(cls, *disp, **kwargs):
    class Admin(admin.ModelAdmin):
        list_display = tuple(d[1:] if d.startswith('-') else d for d in disp) # tuple(f.name for f in cls._meta.get_fields())
        ordering = disp
        # filter_horizontal = ('presents', )
        # formfield_overrides = { models.ManyToManyField: {'widget': CheckboxSelectMultiple}, }

    admin.site.register(cls, Admin)

add(Group, '-year', 'name')
add(Session, 'group', 'beg', 'end')
add(Student, '-group', 'first_name', 'last_name', 'email', 'classe')
# add(Presence, 'student', 'session')

# admin.site.site_title = 'Gestion des présences au paracolaire'
admin.site.site_header = 'Gestion des présences au paracolaire'
# admin.site.index_title = 'Tables'
