from flask import flash, redirect, render_template, url_for
from app import app 
from forms import RegistrationForm, LoginForm
from app.models import User, Post


posts= [
    {  
        'author':'Adil Ahsan',
        'title':'I started making Python Web App in January 2022',
        'content':'First blog content',
        'date_posted':'Jan, 21, 2022',
    },
    { 
        'author':'Umair Javed',
        'title':'Blog post 2',
        'content':'Second blog content',
        'date_posted':'Jan, 22, 2022',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')    

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)   

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin12345':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        
        else:
            flash('Login unsuccessful - Please enter correct email and password', 'danger')
    return render_template('login.html', title='Login', form=form)  

      