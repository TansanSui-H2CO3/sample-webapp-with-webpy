import web
import subapp1
import subapp2

render = web.template.render('templates/')

urls = (
    "/subapp1", subapp1.subapp1,
    "/subapp2", subapp2.subapp2,
    "/", "index",
    "/redirect", "redirect"
)

class index:
    def GET(self):
        return render.index()

class redirect:
    def GET(self):
        raise web.seeother("/")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()