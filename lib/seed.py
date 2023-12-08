from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant,Review,Customer

# Assuming you've set up your database engine and session
engine = create_engine('sqlite:///Challange.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating instances
restaurant1 = Restaurant(name='Restaurant A', price=4)
restaurant2 = Restaurant(name='Restaurant B', price=5)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

# Adding instances to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

# Committing changes
session.commit()
