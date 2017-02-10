import webhose #API Webhose

API_KEY="742c6bef-8c0c-4b44-90a3-2d68f982b166"
# Key proporcionada por WebHouse
class Search:

    def __init__(self):
        webhose.config(token=API_KEY)

    def NextSearch(self, input):
         r = webhose.search( input )
         print r.total

         for post in r:
             print post.language
             print post.title
             r = r.get_next()
