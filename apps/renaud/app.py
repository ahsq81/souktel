#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

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

    keyword.prefix = ['renaud']
    @keyword(r'(\w+) ([Y|N])')
    def testing(self, message, text , exist):
        if exist == 'Y':
            message.respond(u"Hello %s. Thank you" % text)
        else :
            message.respond(u"Not Exist")
        return True

    keyword.prefix = ''
    @keyword(r'multi ([0-9]+) ([0-9]+)')
    def multi(self,message, v1, v2):
       message.respond(u" %s * %s = %s" % (v1 ,v2, int(v1) * int(v2)) )
       return True