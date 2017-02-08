import webhose
import unittest

API_KEY="742c6bef-8c0c-4b44-90a3-2d68f982b166"
webhose.config(token=API_KEY)
r = webhose.search("  weed")
print r.total

for post in r:

    print post.language
    print post.title
    r = r.get_next()