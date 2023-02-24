from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    username = Column(String)


class Categorie(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(30))
    content = Column(String(500))
    preview_image_url = Column(String)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(100))
    up_votes = Column(Integer)
    down_votes = Column(Integer)


# connect to db
engine = create_engine('sqlite:///blog.db')

# create all tables
Base.metadata.create_all(engine)

# start a session
Session = sessionmaker(bind=engine)
session = Session()

# add into table
users = [User(first_name='John', last_name='Snow', email='jsnow99@gmail.com', username='john_the_only'),
         User(first_name='Billy', last_name='White', email='billy@gmail.com', username='billy'),
         User(first_name='Jessy', last_name='Caron', email='jcaron@gmail.com', username='jess_caron')]

categories = [Categorie(name='food'),
              Categorie(name='travel'),
              Categorie(name='finance')]

articles = [Article(category_id='1',
                    author_id='2',
                    title='Eat this awesome magic food and never get fat',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eleifend volutpat ipsum.',
                    preview_image_url='https://cdn.vox-cdn.com/thumbor/KJjKfCBX0DEu7QY7395Sc8fdYBY=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/23957266/Le_Fantome.jpg'),
            Article(category_id='3',
                    author_id='1',
                    title='How to be a billionaire in under 1 minute',
                    content='Maecenas efficitur felis sapien, eget commodo massa vulputate eu. Mauris lobortis elit tortor, eu pharetra tellus tincidunt eget.',
                    preview_image_url='https://static01.nyt.com/images/2018/08/26/business/26VIEW.illo/26VIEW.illo-videoSixteenByNineJumbo1600.jpg'),
            Article(category_id='2',
                    author_id='3',
                    title='Things you should know about travel planning',
                    content='Curabitur convallis neque eu ligula volutpat, id fermentum enim interdum. Curabitur ac justo viverra, vestibulum turpis interdum, aliquet eros.',
                    preview_image_url='https://travellforlife.com/wp-content/uploads/2020/12/tfl_final-09-removebg-preview.png')]

comments = [Comment(article_id='3', author_id='1', message='Thanks, great article!', up_votes='5', down_votes='0'),
            Comment(article_id='1', author_id='2', message='This really worked for me!', up_votes='10', down_votes='7'),
            Comment(article_id='2', author_id='3', message='Wow, so easy and it all works!', up_votes='3', down_votes='7')]


session.add_all(users)
session.add_all(categories)
session.add_all(articles)
session.add_all(comments)

session.commit()
