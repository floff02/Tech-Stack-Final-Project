from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector, json

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = 'your_secret_key'

# Connect to the database
cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              password='X#n!WNnZKIPh7LCk',
                              database='pspstudent')



# Setup routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def homerender():
    return render_template('index.html')

@app.route('/employer')
def employerrender():
    try:
        cursor = cnx.cursor()
        query = 'SELECT * FROM student'
        cursor.execute(query)
        # Fetch the results
        students = cursor.fetchall()
        return render_template('employer.html', students=students)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(students) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/student')
def studentrender():
    return render_template('student.html')

@app.route('/student', methods=['POST'])
def studentprofile():
    # Get the user's input from the form
    studentfname = request.form['ForeName']
    studentsname = request.form['SurName']
    studentpassword = request.form['Password']
    studentemail = request.form['Email']
    studentcareer = request.form['Career']
    studentemp = request.form['Employed']
    studentexp = request.form['Experience']
    cursor = cnx.cursor()
    query = 'INSERT INTO student (studentfname, studentsname, studentpassword, studentemail, studentcareer,  studentemp, studentexp) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (studentfname, studentsname, studentpassword, studentemail, studentcareer, studentemp, studentexp))
    cnx.commit()
    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)