import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", password="password")
        if form.name=="swarna" and form.password=="swarna":
            greeting = "%s" % (form.name.upper())
            return render.index(greeting = greeting)
        else:
        	greeting = "%s, %s" % (form.name, form.password)
        	return render.hello_form()

if __name__ == "__main__":
    app.run()