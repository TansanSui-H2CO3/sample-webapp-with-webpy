import web

urls = (
    "", "redirect",
    "/", "index"
)

class index:
    def GET(self):
        return "Hello! This is sub-application 1!"

class redirect:
    def GET(self):
        raise web.seeother("/")

subapp1 = web.application(urls, globals())