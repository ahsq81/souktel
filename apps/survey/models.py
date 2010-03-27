#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin

''' Survey Models '''

from django.db import models
from django.utils.translation import ugettext_lazy as _

class SrActivity(models.Model) :
    ''' This is the SrActivity models
    its use to store the activity as a dicionary activity code and description

    '''

    code =   models.CharField(max_length=5, unique=True,verbose_name=_(u"Activity Code"))
    name =   models.CharField(max_length=20,verbose_name=_(u"Activity description"))

    def __unicode__(self):
	    return u"%s (%s)" % (self.code, self.name)

class SrProfile(models.Model) :
    '''
    this is the SrProfile
    it use to store the the member informations

    '''

    first_name = models.CharField(max_length=20,verbose_name=_(u"the first name"))
    last_name=   models.CharField(max_length=20,verbose_name=_(u"the last name"))
    sex=   models.CharField(max_length=1,verbose_name=_(u"member gender"))
    age=   models.DecimalField(max_digits=2, decimal_places=0,verbose_name=_(u"member age"))
    activity=   models.ForeignKey(SrActivity,blank=True,verbose_name=_(u"Activity"))
    date = models.DateField(verbose_name=_(u"Date of entry"))

    def __unicode__(self):
	    return u"%s (%s)" % (self.first_name, self.last_name)


