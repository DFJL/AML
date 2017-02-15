
#!/usr/bin/env python

import unittest
import os
import webhose
import time
API_KEY="1dfd4505-f6bc-410e-9ee7-2dff661dae66"

class NextTestCase():
    def __init__(self):
        webhose.config(token=API_KEY)

    def test_next(self, input):

        r = webhose.search(input)
        print r.total
        while True:
            i=0
            for post in r:
                i+=1
                print i
                print post.title #Post Title
                print post.text # Post body text
                print post.language # Post language
                print post.url # Post URL
                print post.author # Post Autor
                print post.rating

                time.sleep(15)
            #r = r.get_next()



if __name__ == "__main__":
    Test= NextTestCase()
    Test.test_next("WEED")