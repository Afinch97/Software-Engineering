import flask

app = flask.Flask(__name__)

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@bp.route("/funfact")
def funfact():
    facts = [
        "Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831.",
        "The heart of the blue whale, the largest animal on earth, is five feet long and weighs 400 pounds.",
        "The word “strengths” is the longest word in the English language with only one vowel.",
    ]
    return flask.jsonify(facts)


app.register_blueprint(bp)

app.run()
