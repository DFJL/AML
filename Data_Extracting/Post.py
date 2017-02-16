#!/usr/bin/env pyh
import codecs
class Post:

    def __init__(self, title,language,body_text, site):
        self.title=title
        self.body_text=body_text
        self.site=site
        self.language=language

    def __str__(self):
        return "\n Title : %s  , \n Language : %s , \n Site : %s  , \n Body text : %s " % ( self.title.encode('utf-8'), self.language.encode('utf-8') , self.site.encode('utf-8') , self.body_text.encode('utf-8'))