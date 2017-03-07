#!/usr/bin/env python
import unittest
import os
import webhoseio
import time
import Post
import GlobalData

class NextTestCase():
    def __init__(self):
        webhoseio.config(token=GlobalData.API_KEY)


    def test_next(self, input):
        output = webhoseio.query("filterWebData", {"q": input+ "language:(english) OR language:spanish "})

        print output['totalResults']
        i=0
        while True:
            for post in output['posts']:
                i=i+1
                print i
                title = post['title'] #Post Title
                body_text = post['text'] # Post body text
                language = post['language'] # Post language
                url = post['url']
                Test = Post.Post(title,language,body_text,url)
                print Test
                """print post.author # Post Autor
                print post.rating
                print post.external_links
                print post.crawled
                print post.published
                time.sleep(0.55)"""
            time.sleep(10)
            output = webhoseio.get_next()


