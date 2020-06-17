from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__,template_folder="template")


#import secrets module in it run code secrets.token_hex(16)
app.config['SECRET_KEY'] = '23553452bd8ca3b4e1267e778905ea1b'


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','sucess')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.email.data =='admin@blog.com' and form.password.data =='password':
        flash('you have been logged in !','success')
        return redirect(url_for('home'))
    else:
        flash('login Unsuccessful.please check username and password','danger')
    return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)