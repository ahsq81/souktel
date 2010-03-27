# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Ahmad"
__date__ ="$Mar 24, 2010 11:50:05 AM$"

#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin
'''
    Survey Main models to handle the survey opperation and mintain them
'''

import rapidsms
import time
import datetime

from rapidsms.parsers.keyworder import Keyworder   # this library use to handel the user command
from django.utils.translation import ugettext as _ # this library use to allow the translation appility base on useing "_" before the string to translate

from models import SrProfile
from models import SrActivity

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):
        '''  finds out corresponding function and call it '''
        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            #message.respond(u"Unrecognised message")
            return False
        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(_(u"System encountered an Error: %s") % e)
            return True

    keyword.prefix = ['help', _(u"help")]
    @keyword(r'')
    def helpme(self, message):
        '''
        the help function "helpme" this funnction work when user send the keyword help to show him
        the format and the instruction supported in our services

        '''
        message.respond(_(u"INS f-name l-name (gend){M|F} age Activity; FIND activity find all member register with that activity; STAT return the number of register member"))
        return True



    keyword.prefix = ['INS',_(u"INS")]  # handling INS world

    @keyword(r'(\w+) (\w+) (\w+) ([0-9]+) (\w+)')

    def insert(self,message, fname, lname, sex, age, activity):
        '''
        the ins function "insert" this funnction work when user send the keyword INS in the following format
        INS "first name" "last name" gender age activety
        to store the information into the database table SaProfile
        '''

        ''' check if the gender format M|F correct'''
        if sex.lower() not in ('m','f',_(u'm'),_(u'f')):
            message.respond(_(u"Gendr not support"))
        try:
            activity_obj = SrActivity.objects.get(code=activity.strip().lower() )
        except Exception, e:
             message.respond(_(u"1-System encountered an Error: %s") % e)
             return False

        ins = SrProfile(first_name = fname, last_name=lname,sex = sex.upper() ,age= int(age) ,activity = activity_obj, date = datetime.date.today())
        try:
            ins.save()
            message.respond(_(u"Recourd saved.."))
        except Exception, e:
            message.respond(_(u"2-System encountered an Error: %s") % e)
            return True



    keyword.prefix = ['FIND',_(u"FIND")]
    @keyword(r'(\w+)')
    def find(self,message, activity):
        '''
        the find function "find" this funnction work when user send the keyword find in the following format
        find "activety code"
        to list all member they share the same activity from the database table SaProfile
        '''
        try:
            activity_obj = SrActivity.objects.get(code=activity.strip().lower() )
        except Exception, e:
             message.respond(_(u"1-System encountered an Error: %s") % e)
             return False

        try:
            SrProfile_opj = SrProfile.objects.filter(activity = activity_obj)
            all_profile = []  # all the recourd will fill on side this array
            for profile in SrProfile_opj:
                ''' fetching the database record " first and last name " into the array'''
                all_profile.append(profile.first_name + " " + profile.last_name)
            message.respond(_(u"The Result found:%s") % u", ".join(all_profile))
        except Exception, e:
            message.respond(_(u"2-System encountered an Error: %s") % e)
        return True

  

    keyword.prefix = ['STAT',_(u"stat")]
    @keyword(r'')
    def status(self,message):
        '''
        the stat function "status" this funnction work when user send the keyword stat
        to return the number of register member on the SeProfile table
        '''
        try:
            SrProfile_obj = SrProfile.objects.all()
            message.respond(_(u"Number of entry:%s") % SrProfile_obj.count())
        except Exception, e:
            message.respond(_(u"2-System encountered an Error: %s") % e)
        return True