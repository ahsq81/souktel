#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin


from django.db import models


class SrActivity(models.Model) :

    code =   models.CharField(max_length=5, unique=True)
    name =   models.CharField(max_length=20)

    def __unicode__(self):
	    return u"%s (%s)" % (self.code, self.name)

class SrProfile(models.Model) :

    first_name = models.CharField(max_length=20)
    last_name=   models.CharField(max_length=20)
    sex=   models.CharField(max_length=1)
    age=   models.DecimalField(max_digits=2, decimal_places=0)
    activity=   models.ForeignKey(SrActivity,blank=True)
    date = models.DateField()

    def __unicode__(self):
	    return u"%s (%s)" % (self.first_name, self.last_name)


