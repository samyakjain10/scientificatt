from flask import Flask, request, render_template, redirect, Blueprint, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/scientificatt'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

dashboard = Blueprint('login', __name__, url_prefix='/dashboard')  # admin   branch-head   employee
branch = Blueprint('branch', __name__, url_prefix='/branches')  # admin
department = Blueprint('department', __name__, url_prefix='/departments')  # admin


# employee = Blueprint('employee',__name__, url_prefix='/employee')                               #  admin   branch-head
# assign_project = Blueprint('assign_project',__name__, url_prefix='/assign-project')             #  admin   branch-head
# assign_department = Blueprint('assign_department',__name__, url_prefix='/assign-department')    #  admin   branch-head

class Employees(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(80))
    branch = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(30), nullable=False)
    designation = db.Column(db.String(30), nullable=False)


class Branches(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    head = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)


class Departments(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)


class Projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    employee = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)


class New(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(employee_id):
    return Employees.query.get(employee_id)

#DEBUG REMEMBER ME
@app.route('/', methods=['GET', 'POST'])
def login():
    # Take care of security while logging in
    # set session variable for email
    # fetch designation from  employees table to direct to correct dashboard
    if current_user.is_authenticated:
        if current_user.designation == 'Founder':
            return redirect('/dashboard/admin/')
        elif current_user.designation == 'Branch Head':
            return redirect('/dashboard/branch_head/')
        else:
            return redirect('/dashboard/employee/')
    elif request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        remember_me = request.form.get('remember_me')
        employee = Employees.query.filter_by(email=username).first()
        if employee:
            if check_password_hash(employee.password, password):
                login_user(employee, remember=remember_me)
                flash('Logged in successfully.')
                if employee.designation == 'Founder':
                    return redirect('/dashboard/admin/')
                elif employee.designation == 'Branch Head':
                    return redirect('/dashboard/branch_head/')
                else:
                    return redirect('/dashboard/employee/')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@dashboard.route('/admin/')
def admin_dashboard():
    # filter by all projects
    # show active projects first and then completed ones as well
    # add project option
    # open project on a new page after clicking on the project card and the page should have the options for assigning people edit and delete
    # edit page should display a table of currently assigned employees with an option to delete them
    # assign page should have a dropdown with a list of all the employees to select from them
    project1 = Projects.query.filter_by(status='ACTIVE').all()
    project2 = Projects.query.filter_by(status='COMPLETED').all()
    return render_template('founder_module.html', project1=project1, project2=project2, user=current_user)


@dashboard.route('/branch_head/')
def branch_head_dashboard():
    # add project option
    # open project on a new page after clicking on the project card and the page should have the options for assigning people edit and delete
    # edit page should display a table of currently assigned employees with an option to delete them
    # assign page should have a dropdown with a list of all the employees to select from them
    # either create session variable of branch and use it to fetch projects of the branch to display to the branchhead
    # Or fetch branch from employee table using filter with sno = session['sno'] and then use branch of that employee i.e. employee.branch to filter projects
    project1 = Projects.query.filter((Projects.branch==current_user.branch)&(Projects.status=='ACTIVE')).all()
    project2 = Projects.query.filter((Projects.branch==current_user.branch)&(Projects.status=='COMPLETED')).all()
    return render_template('state_head_module.html', user=current_user ,project1=project1, project2=project2)


@dashboard.route('/employee/')
def employee_dashboard():
    # filter projects using email of the respective person
    project = Projects.query.filter_by(employee=current_user.email).all()
    return render_template('employee_module.html', project=project, user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register_employee():
    # check if the user is in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user'] ==:
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        passw = request.form.get('password')
        password = generate_password_hash(passw, method='sha256')
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
    # query department and branches from table
    total_branches = Branches.query.filter_by().all()
    total_departments = Departments.query.filter_by().all()
    total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]

    return render_template('register.html',
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_designations=total_designations, user=current_user)


@app.route('/register_login', methods=['GET', 'POST'])
def register_login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_no')
        branch = request.form.get('branch')
        passw = request.form.get('pass')
        password = generate_password_hash(passw, method='sha256')
        entry = New(name=name,
                    email=email,
                    password=password,
                    phone_no=phone)
        db.session.add(entry)
        db.session.commit()
        return render_template('login.html')
    else:
        total_branches = Branches.query.filter_by().all()
        return render_template('register_login.html', total_branches=total_branches)


@app.route('/new', methods=['GET', 'POST'])
def new():
    # display table of employees with department or branch as not assigned also need to make frontend tempplate
    # name email branch department (designation) assign delete
    employees = New.query.filter_by().all()
    total_branches = Branches.query.filter_by().all()
    return render_template('new.html', employees=employees, user=current_user, total_branches=total_branches)


@app.route('/add', methods=['GET','POST'])
def add():
    # sno, name, department, employee, branch, date, status, description
    if request.method == 'POST':
        name = request.form.get('name')
        employee = request.form.get('employee')
        description = request.form.get('description')
        status = request.form.get('status')
        branch = request.form.get('branch')
        department = request.form.get('department')
        date = datetime.now()
        entry = Projects(name=name,
                          employee=employee,
                          description=description,
                          status=status,
                          branch=branch,
                          department=department,
                          date=date)
        db.session.add(entry)
        db.session.commit()
    # query department and branches from table
    total_branches = Branches.query.filter_by().all()
    total_departments = Departments.query.filter_by().all()
    total_status = ['ACTIVE', 'COMPLETED']

    return render_template('add.html',
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_status=total_status, user=current_user)


# change and make as per blueprint for founder and branchhead
@app.route('/employee')
def employee():
    employees = Employees.query.filter_by().all()
    return render_template('employee.html', employees=employees, user=current_user)


@app.route('/employee_edit/<string:id>', methods=['GET', 'POST'])
def employee_edit(id):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        branch = request.form.get('branch')
        department = request.form.get('department')
        designation = request.form.get('designation')
        db.session.query(Employees).filter_by(id=id).update(dict(name=name,
                                                                 email=email,
                                                                 phone=phone,
                                                                 branch=branch,
                                                                 department=department,
                                                                 designation=designation))

        db.session.commit()
        return redirect('/employee')
    employees = Employees.query.filter_by(id=id).first()
    total_branches = Branches.query.filter_by().all()
    total_departments = Departments.query.filter_by().all()
    total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]
    return render_template('employee_edit.html', employee=employees,
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_designations=total_designations, user=current_user)


@app.route('/employee_delete/<string:id>', methods=['GET', 'POST'])
def employee_delete(id):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
    employee = Employees.query.filter_by(id=id).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect('/employee')


@branch.route('/')
def branches():
    # display branches table only to founder
    # Create edit add delete options with separate pages i.e. create frontend for edit  and add
    branches = Branches.query.filter_by().all()
    return render_template('branches.html', branches=branches, user=current_user)


@branch.route('/edit/<string:sno>', methods=['GET', 'POST'])
# value repeating in dropdown(delhi delhi)
# update queries (for designation) accodingly if
# 1. branch-head is changed
# 2. branch is deleted
def edit_branch(sno):
    if request.method == 'POST':
        name = request.form.get('name')
        head = request.form.get('head')
        address = request.form.get('address')
        db.session.query(Branches).filter_by(sno=sno).update(dict(name=name,
                                                                  head=head,
                                                                  address=address, ))

        db.session.commit()
        return redirect('/branch')
    branch = Branches.query.filter_by(sno=sno).first()
    total_heads = Employees.query.filter_by(branch=branch.name).all()
    return render_template('branch_edit.html', branch=branch, total_heads=total_heads, user=current_user)


@branch.route('/delete/<string:sno>', methods=['GET', 'POST'])
def branch_delete(sno):
    branch = Branches.query.filter_by(sno=sno).first()
    db.session.delete(branch)
    db.session.commit()
    return redirect('/branch')


@department.route('/')
def departments():
    # display departments table only to founder
    # Create add and delete
    # create add by toggle option or drop down or drop down form
    departments = Departments.query.filter_by().all()
    return render_template('department.html', departments=departments, user=current_user)


@department.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete_departments(sno):
    department = Departments.query.filter_by(sno=sno).first()
    db.session.delete(department)
    db.session.commit()
    return redirect('/department')


@app.route('/profile')
def profile():
    # use session variable to get email and display details accordingly
    # improve frontend
    # profile edit option
    return render_template('profile.html')


@app.route('/forgot_password')
def forgot_password():
    # think the approach as we have prob with smtp server while hosting so cant send emails
    pass


app.register_blueprint(dashboard)
app.register_blueprint(branch)
app.register_blueprint(department)
app.run(debug=True)

# improve profile frontend
# improve logo on left top corner frontend
# add footer with privacy policy
# change card frontend
