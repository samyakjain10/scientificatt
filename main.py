from flask import Flask, escape, request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/scientificatt'
db = SQLAlchemy(app)

class Employees(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(30), nullable=False)
    designation = db.Column(db.String(30), nullable=False)

@app.route('/')
def dashboard5():
    return render_template('login.html')

@app.route('/employee_module')
def dashboard4():
    return render_template('employee_module.html')

@app.route('/founder')
def dashboard3():
    return render_template('founder_module.html')

@app.route('/register', methods = ['GET','POST'])
def register_employee():

    if(request.method=='POST'):
       name = request.form.get('name')
       email = request.form.get('email')
       phone = request.form.get('phone')
       password = request.form.get('password')
       branch = request.form.get('branch')
       department = request.form.get('department')
       designation = request.form.get('designation')
       entry = Employees(name=name,
                        email=email,
                        phone=phone,
                        password=password,
                        branch=branch,
                        department=department,
                        designation=designation)
       db.session.add(entry)
       db.session.commit()

    total_branches = [{'branch':'delhi'},{'branch':'mumbai'}]
    total_departments = [{'department': 'marketing'}, {'department': 'hr'}]
    total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]

    return render_template('register.html',
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_designations=total_designations)

@app.route('/state')
def dashboard1():
    return render_template('state_head_module.html')

@app.route('/layout')
def dashboard6():
    return render_template('layout.html')

@app.route('/profile')
def dashboard7():
    return render_template('profile.html')

@app.route('/department')
def dashboard8():
    return render_template('department.html')

@app.route('/branch')
def branch():
    return render_template('branches.html')

@app.route('/employee')
def employee():
    employees = Employees.query.filter_by().all()
    return render_template('employee.html',employees=employees)

@app.route('/register_login')
def dashboard11():
    return render_template('register_login.html')


app.run(debug=True)