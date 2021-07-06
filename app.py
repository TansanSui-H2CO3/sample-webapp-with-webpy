import web

render = web.template.render('templates/')

urls = (
    "/", "index",
    "/redirect", "redirect",
    "/greeting/(.*)", "greeting"
)

class index:
    def GET(self):
        return render.index()

class redirect:
    def GET(self):
        raise web.seeother("/")

class greeting:
    def GET(self, name):
        return render.indexWithParameter(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()