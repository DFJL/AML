#!/usr/bin/env python
class Post:

    def __init__(self, title,language,body_text, site):
        self.title=title
        self.body_text=body_text
        self.site=site
        self.language=language

    def __str__(self):
        return "Title : %s  , Language : %s , Body Text : %s  " % ( self.title, self.language , self.body_text)