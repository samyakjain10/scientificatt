from flask import Flask, escape, request,render_template,session,redirect
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
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register_employee():
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user'] ==:
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


@app.route('/register_login',methods=['GET','POST'])
def register_login():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_no')
        password = request.form.get('pass')
        entry = Employees(name=name,
                        email=email,
                        phone=phone,
                        password=password,
                        branch="NOT ASSIGNED",
                        department="NOT ASSIGNED",
                        designation="Employee")
        db.session.add(entry)
        db.session.commit()
        return render_template('login.html')
    else:
        return render_template('register_login.html')


@app.route('/employee_f')
def employee_founder_module():
    employees = Employees.query.filter_by().all()

    return render_template('employee.html',employees=employees)

@app.route('/employee_f_edit/<string:sno>',methods=['GET','POST'])
def employee_f_edit(sno):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
        if request.method=='POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            password = request.form.get('password')
            branch = request.form.get('branch')
            department = request.form.get('department')
            designation = request.form.get('designation')
            employees = Employees.query.filter_by(sno=sno).all()
            employees.name=name
            employees.email=email
            employees.phone=phone
            employees.password=password
            employees.branch=branch
            employees.department=department
            employees.designation=designation
            db.session.commit()
            return redirect('/employee_f_edit/'+sno)
        employees = Employees.query.filter_by(sno=sno).all()
        total_branches = [{'branch': 'delhi'}, {'branch': 'mumbai'}]
        total_departments = [{'department': 'marketing'}, {'department': 'hr'}]
        total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]
        return render_template('employee_edit.html',employee=employees,
                               total_branches=total_branches,
                               total_departments=total_departments,
                               total_designations=total_designations)


@app.route('/employee_f_delete/<string:sno>',methods=['GET','POST'])
def employee_delete(sno):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
        employee=Employees.query.filter_by(sno=sno).first()
        db.session.delete(employee)
        db.session.commit()
        return redirect('/employee_f')

app.run(debug=True)