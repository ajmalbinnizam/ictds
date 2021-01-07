from flask import Flask, request, session, render_template, g
import sqlite3
app = Flask(__name__)

#app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret!'

def connect_db():
    sql = sqlite3.connect('D:/data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello, World!</h1>'


@app.route('/theform', methods=['GET', 'POST'])
def theform():

    if request.method == 'GET':
        return render_template('form.html')
    else:
        SN = request.form['SN']
        SL = request.form['SL']
        SW = request.form['SW']
        PL = request.form['PL']
        PW = request.form['PW']


        db = get_db()
        db.execute('insert into iris (SN, SL, SW, PL, PW ) values (?, ?, ?, ?, ?)', [SN,SL,SW,PL,PW])
        db.commit()

        return '<h1>Serial Number {}. \
                     Sepal Length {}. \
                     Sepal Width {}. \
                     Petal Length {}. \
                     Petal Width {}. \
                     You have submitted the form successfully! <h1>'.format(SN, SL, SW, PL, PW)


@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select * from iris')
    results = cur.fetchall()
    return '<h1>SN {}. SL {}. SW {}. PL {}. PW {}. </h1>'.format(results[0]['SN'],
                                                                results[0]['SL'],
                                                                results[0]['SW'],
                                                                 results[0]['PL'],
                                                                 results[0]['PW'])


if __name__ == '__main__':
    app.run()