from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import db,login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    bio  = db.Column(db.String(255),default='My default Bio')
    nickname  = db.Column(db.String(255),unique=True,nullable=True)
    # location  = db.Column(db.String(255),unique=True,nullable=True)
    profile_pic_path = db.Column(db.String(255),default='default.png')
    hashed_password = db.Column(db.String(255),nullable=False)
    case = db.relationship('Case',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f"User {self.username}"

class Case(db.Model):
    __tablename__='cases'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment',backref='case',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='case',lazy='dynamic')

    def save_cases(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_case(cls,id):
        cases = Case.query.get(id)
        return cases
    

    def __repr__(self):
        return f'Case {self.post}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    case_id = db.Column(db.Integer,db.ForeignKey('cases.id'))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,case_id):
        comments = Comment.query.filter_by(case_id=case_id).all()
        return comments
    def __repr__(self):
        return f'Case {self.post}'

class Upvote(db.Model):
    __tablename__='upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    case_id = db.Column(db.Integer,db.ForeignKey('cases.id'))

    def save_votes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,id):
        votes = Upvote.query.filter_by(case_id=id).all()
        return votes

    def __repr__(self):
        return f'{self.user_id}:{self.case_id}'


