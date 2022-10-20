from flask import Flask, render_template, request, redirect, url_for
import checker

app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def Home():
    if request.method == 'POST':
        id = request.form['certificate_id']
        if len(id)>0:
            return redirect(url_for('verify',id = id))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/verification/<id>")
def verify(id):
    if checker.checker(id):
        (Name, Institute, Event) = checker.data(id)
        return render_template('verification.html', Name=Name, Institute=Institute, Event=Event)
    else:
        return "<h1>Does not Exist</h1>"

app.run(debug=True, host="0.0.0.0", port=8080)
