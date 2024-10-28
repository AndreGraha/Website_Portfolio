from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/about")
def about():
    return render_template('about.html', title ='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/projects")
def projects_page():
    return render_template('projects.html', title='Projects')

@app.route("/projects/predicting-heart-disease")
def predicting_heart_disease():
    return render_template('projects/predicting_heart_disease.html',title='Predicting Heart Disease')



if __name__ == '__main__':
    app.run()