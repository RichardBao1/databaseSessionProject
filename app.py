from flask import Flask
import data_access

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    fname = input("Enter first name: ")
    sname = input("Enter surname: ")
    data_access.addUser(fname, sname)
    sname = input("Enter surname to search for: ")
    data_access.findSurname(sname)


    return 'Hello World!'


@app.route('/addStudent', methods=['GET', 'POST']):
def addStudent():
    form=forms.StuDetailsForm()
    if form.validate_on_submit():
        session['fName'] = form.fName.data
        session['sName'] = form.sName.data
        print(session['fName'])
        data_access.addUser(session['fName'], session['sName'])
        flash(f"{session['fName']} {session['sName']} added")
        return redirect(url_for('index'))
    return render_template('/addStudent.html', form=form)

@app.route('/viewStudents')
def viewStudents():
    students = data_access.query_db('SELECT * FROM students ORDER BY sName COLLATE NOCASE ASC ')
    # Select all from students and sort by surName by Ascii value without regard for upper or lowercase

    return render_template('/viewStudents.html', students=students)

thing

def findStudent():
    form = form.FindStudent()
    if form.validate_on_submit():
        name = form.name.data.upper()
        students = data_access.query_db('SELECT * FROM student WHERE'
                                        'upper(fName)=? OR upper(sname)=?'
                                        'ORDER BY sName COLLATE NOCASE ASC', (name, name)
        )


if __name__ == '__main__':
    app.run()
