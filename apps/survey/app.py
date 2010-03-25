# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Ahmad"
__date__ ="$Mar 24, 2010 11:50:05 AM$"



#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms
import time
import datetime

from rapidsms.parsers.keyworder import Keyworder
from models import SrProfile
from models import SrActivity

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            #message.respond(u"Unrecognised message")
            return False
        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(u"System encountered an Error: %s" % e)
            return True

    def old_handle(self, message):
        ''' not used anymore '''
        if message.text.lower().startswith('renaud'):
            message.respond(u"Hello %s" % message.text)
            return True

        return False

    keyword.prefix = ['help']
    @keyword(r'')
    def helpme(self, message):
        message.respond(u"INS f-name l-name (gend){M|F} age Activity; FIND activity find all member register with that activity; STAT return the number of register member")
        return True

    keyword.prefix = 'INS'
    @keyword(r'(\w+) (\w+) ([M|F]) ([0-9]+) (\w+)')
    def insert(self,message, fname, lname, sex, age, activity):

        try:
            activity_obj = SrActivity.objects.get(code=activity.strip().lower() )
        except Exception, e:
             message.respond(u"1-System encountered an Error: %s" % e)
             return False
        print activity_obj
        ins = SrProfile(first_name = fname, last_name=lname,sex = sex ,age= int(age) ,activity = activity_obj, date = datetime.date.today())
        try:
            ins.save()
            message.respond(u"done!!!")
        except Exception, e:
            message.respond(u"2-System encountered an Error: %s" % e)
            return True

    keyword.prefix = 'FIND'
    @keyword(r'(\w+)')
    def find(self,message, activity):

        try:
            activity_obj = SrActivity.objects.get(code=activity.strip().lower() )
        except Exception, e:
             message.respond(u"1-System encountered an Error: %s" % e)
             return False

        try:
            SrProfile_opj = SrProfile.objects.filter(activity = activity_obj)
            all_profile = []
            for profile in SrProfile_opj:
                all_profile.append(profile.first_name + " " + profile.last_name)
            '''
            mylist ='';
            ind = 0
            for profile in SrProfile_opj:
                if ind  > 0:
                    mylist = mylist + " | "
                    ind = 1

                mylist = mylist + profile.first_name + " " + profile.last_name
            '''
            message.respond(u"The Result found:%s" % u", ".join(all_profile))
        except Exception, e:
            message.respond(u"2-System encountered an Error: %s" % e)
        return True


    keyword.prefix = 'STAT'
    @keyword(r'')
    def status(self,message):

        try:
            SrProfile_opj = SrProfile.objects.all()
            message.respond(u"Number of entry:%s" % len(SrProfile_opj))
        except Exception, e:
            message.respond(u"2-System encountered an Error: %s" % e)
        return True