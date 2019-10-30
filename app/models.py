class User(UserMixin, db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(255),unique=True,nullable=False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    bio  = db.Column(db.String(255),default='My default Bio')
    nickname  = db.Column(db.String(255),unique=True,nullable=False)
    profile_pic_path = db.Column(db.String(255),default='default.png')
    hashed_password = db.Column(db.String(255),nullable=False)
    case = db.relationship('Case',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')