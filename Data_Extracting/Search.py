#!/usr/bin/env python
import unittest
import os
import webhose
import time
import Post
import GlobalData

class NextTestCase():
    def __init__(self):
        webhose.config(token=GlobalData.API_KEY)


    def test_next(self, input):

        r = webhose.search(input)
        print r.total
        i=0
        for post in r:
            i=i+1
            print i
            title = post.title #Post Title
            body_text = post.text # Post body text
            language = post.language # Post language
            url = post.url # Post URL
            Test = Post.Post(title,language,body_text,url)

            print Test
            print post.author # Post Autor
            print post.rating
            print post.external_links
            print post.crawled
            print post.published
            time.sleep(0.55)




