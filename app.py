from flask import Flask, request, render_template , redirect, url_for

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/')
def Contador():
    return render_template("contador.html")



if __name__ == '__main__':
    app.run(debug=True)
