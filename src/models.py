import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)
    text = Column(String(250))
    user_post = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class PostLikes(Base):
    __tablename__ = 'postlikes'
    id = Column(Integer, primary_key=True)
    liked_post = Column(Integer, ForeignKey('post.id'))
    user_who_liked = Column(Integer, ForeignKey('user.id'))

class UserFollower(Base):
    __tablename__ = 'userfollower'
    id = Column(Integer, primary_key=True)
    user_followed = Column(Integer, ForeignKey('user.id'))
    user_following = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e