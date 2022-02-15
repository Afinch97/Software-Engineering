import flask

app = flask.Flask(__name__)
app.secret_key="Super Secret"

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route("/handle_form", methods=["POST"])
def handle_form():
    data = flask.request.form
    campus_id = data["campus_id"]
    if data['campus_id'] == "afinch6":
        return flask.redirect(flask.url_for("welcome"))
    else:
        flask.flash("Wrong Campus ID")
        return flask.redirect(flask.url_for("index"))

@app.route("/other_page")
def welcome():
    return '<h1>Welcome Anthony</h1>'

app.run()