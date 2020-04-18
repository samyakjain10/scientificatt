from flask import Flask, request, render_template, redirect, Blueprint,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/scientificatt'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

dashboard = Blueprint('login', __name__, url_prefix='/dashboard')  # admin   branch-head   employee


# employee = Blueprint('employee',__name__, url_prefix='/employee')                               #  admin   branch-head
# department = Blueprint('department',__name__, url_prefix='/department')                         #  admin
# branch = Blueprint('branch',__name__, url_prefix='/branch')                                     #  admin   branch-head
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


# class Projects(db.Model):
# project name , project assigned to, branch, department,date,status,description
# class Branches(db.Model):
# branch name , branch head, address
# class Departments(db.Model):
# department name, remove total employees from department.html

@login_manager.user_loader
def load_user(employee_id):
    return Employees.query.get(int(employee_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    # Take care of security while logging in
    # set session variable for email
    # fetch designation from  employees table to direct to correct dashboard
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        employee = Employees.query.filter_by(email=username).first()
        if employee:
            if check_password_hash(employee.password, password):
                login_user(employee, remember=True)
                flash('Logged in successfully.')
                if employee.designation == 'Founder':
                    redirect('/dashboard/admin/')
                elif employee.designation == 'Branch Head':
                    redirect('/dashboard/branch_head/')
                else:
                    redirect('/dashboard/employee/')
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
    return render_template('founder_module.html')


@dashboard.route('/branch_head/')
def branch_head_dashboard():
    # add project option
    # open project on a new page after clicking on the project card and the page should have the options for assigning people edit and delete
    # edit page should display a table of currently assigned employees with an option to delete them
    # assign page should have a dropdown with a list of all the employees to select from them
    # either create session variable of branch and use it to fetch projects of the branch to display to the branchhead
    # Or fetch branch from employee table using filter with sno = session['sno'] and then use branch of that employee i.e. employee.branch to filter projects
    return render_template('state_head_module.html')


@dashboard.route('/employee/')
def employee_dashboard():
    # filter projects using email of the respective person
    return render_template('employee_module.html')


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
    total_branches = [{'branch': 'delhi'}, {'branch': 'mumbai'}]
    total_departments = [{'department': 'marketing'}, {'department': 'hr'}]
    total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]

    return render_template('register.html',
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_designations=total_designations)


@app.route('/register_login', methods=['GET', 'POST'])
def register_login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_no')
        passw = request.form.get('pass')
        password = generate_password_hash(passw, method='sha256')
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


@app.route('/new', methods=['GET', 'POST'])
def new():
    # display table of employees with department or branch as not assigned also need to make frontend tempplate
    # name email branch department (designation) assign delete
    pass


# change and make as per blueprint for founder and branchhead
@app.route('/employee')
def employee():
    employees = Employees.query.filter_by().all()
    return render_template('employee.html', employees=employees)


# DEBUG THE FOLLOWING
@app.route('/employee_edit/<string:sno>', methods=['GET', 'POST'])
def employee_edit(sno):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        branch = request.form.get('branch')
        department = request.form.get('department')
        designation = request.form.get('designation')
        employees = Employees.query.filter_by(sno=sno).all()
        employees.name = name
        employees.email = email
        employees.phone = phone
        employees.password = password
        employees.branch = branch
        employees.department = department
        employees.designation = designation
        db.session.commit()
        return redirect('/employee_edit/' + sno)
    employees = Employees.query.filter_by(sno=sno).all()
    total_branches = [{'branch': 'delhi'}, {'branch': 'mumbai'}]
    total_departments = [{'department': 'marketing'}, {'department': 'hr'}]
    total_designations = [{'designation': 'Founder'}, {'designation': 'Branch Head'}, {'designation': 'Employee'}]
    return render_template('employee_edit.html', employee=employees,
                           total_branches=total_branches,
                           total_departments=total_departments,
                           total_designations=total_designations)


@app.route('/employee_delete/<string:id>', methods=['GET', 'POST'])
def employee_delete(id):
    # check if user in session part to be activates once we complete dashboard login part and thus set the session variable
    # if user in session and session['user']== :
    employee = Employees.query.filter_by(id=id).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect('/employee')


@app.route('/branches')
def branches():
    # display branches table only to founder
    # Create edit add delete options with separate pages i.e. create frontend for edit  and add
    pass


@app.route('/departments')
def departments():
    # display departments table only to founder
    # Create add and delete
    # create add by toggle option or drop down or drop down form
    pass


@app.route('/profile')
def profile():
    # use session variable to get email and display details accordingly
    # improve frontend
    # profile edit option
    pass


@app.route('/forgot_password')
def forgot_password():
    # think the approach as we have prob with smtp server while hosting so cant send emails
    pass


app.register_blueprint(dashboard)
app.run(debug=True)

# improve profile frontend
# improve logo on left top corner frontend
# add footer with privacy policy
# change card frontend
