import web

urls = (
    "", "redirect",
    "/", "index"
)

class index:
    def GET(self):
        return "Hello! This is sub-application 2!"

class redirect:
    def GET(self):
        raise web.seeother("/")

subapp2 = web.application(urls, globals())