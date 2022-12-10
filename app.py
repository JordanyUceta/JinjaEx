from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story 


app = Flask(__name__) 
app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app) 

@app.route('/')
def home_page(): 

    prompts = story.prompts

    return render_template("base.html", prompts = prompts)

@app.route('/story')
def story_page(): 

    text = story.generate(request.args)

    return render_template('story.html', text = text)