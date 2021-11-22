from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail  #this is for mail





'''import config.json file '''
with open('config.json' , 'r') as c:
    params = json.load(c)["params"]

local_server=True

app = Flask(__name__)

# this is for mailing configuration
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']

)
app.config['SECRET_KEY'] = "Your_secret_string"
mail = Mail(app)



# to configure the DB

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingslasher'      #this is for DATAbase url 'mysql://user:password@localhost/db_name'

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_url']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_url']



db = SQLAlchemy(app)

class Contact(db.Model):
    # sno ,name ,email , phone ,msg
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.Integer(), unique=False, nullable=False)
    msg = db.Column(db.String(200), unique=False, nullable=False)
    date= db.Column(db.Integer(), unique=False, nullable=False)


class Posts(db.Model):
    # sno ,name ,email , phone ,msg
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    date= db.Column(db.Integer(), unique=False, nullable=False)




#to navigate the page

@app.route("/index")
def home():
    posts = Posts.query.filter_by().all()[0:params['no_post']]
    return render_template('index.html',params=params ,posts=posts )


@app.route("/about")
def about():
    return render_template('about.html',params=params)


@app.route("/contact", methods= ['GET','POST'])
def contact():
    if (request.method== 'POST'):
        '''Fetch data and add it to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')

        '''this is for entering the values in DB and add them in db table and commit db'''
        entry = Contact(name=name , email=email ,phone = phone , msg= msg ,date=datetime.now())
        db.session.add(entry)
        db.session.commit()

        '''this is for email configuration'''
        mail.send_message('New Msg from '+ name,
                          sender=email,
                          recipients=[params['gmail-user'] , email],
                          body = msg + "\n phone num:" + phone

                          )

    return render_template('contact.html',params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post= Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html',params=params ,post=post)


'''this is for the dash board part '''
@app.route("/dashboard" ,methods=['GET','POST'])
def dashboard():
    if request.method =='POST' :

        '''if the user is already logged in'''
        if 'user' in session and session['user'] == params['admin_user'] :
            post = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=post)


        '''enter admin pannel   '''

        username = request.form.get('uname')
        password = request.form.get('pass')
        if((username == params['admin_user'])and (password == params['admin_password'])):

            #set this session var
            session['user'] = username             #this is for user session is on
            post = Posts.query.all()
            return render_template('dashboard.html', params=params ,posts=post  )
    else:
        return render_template('login.html', params=params)




app.run(debug=True)