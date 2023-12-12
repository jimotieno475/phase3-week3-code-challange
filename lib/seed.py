from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant,Review,Customer


if __name__ == '__main__':
    # Assuming you've set up your database engine and session
    engine = create_engine('sqlite:///migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # Creating instances
     
    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.query(Customer).delete()

    restaurant1 = Restaurant(name='Koin ', price=500)
    restaurant2 = Restaurant(name='Barclay', price=450)
    restaurant3 = Restaurant(name='wagwan ', price=600)
    restaurant4 = Restaurant(name='jungle', price=540)
    restaurant5 = Restaurant(name='winoow ', price=700)
    restaurant6 = Restaurant(name='Gozin', price=850)
    restaurant7 = Restaurant(name='degozns ', price=200)
    restaurant8 = Restaurant(name=' Wiper', price=350)

 

    customer1 = Customer(first_name='John', last_name='Doe')
    customer2 = Customer(first_name='Jane', last_name='Smith')
    customer3 = Customer(first_name='joy', last_name='Doe')
    customer4 = Customer(first_name='king', last_name='Smith')
    customer5 = Customer(first_name='ban', last_name='Doe')
    customer6 = Customer(first_name='Reso', last_name='Smith')
    customer7 = Customer(first_name='Rose', last_name='Doe')
    customer8 = Customer(first_name='Jaba', last_name='Smith')
    customer9 = Customer(first_name='Jully', last_name='Doe')
    customer10 = Customer(first_name='wire', last_name='Smith')
    customer11= Customer(first_name='Bods', last_name='Doe')
    customer12 = Customer(first_name='Waren', last_name='Smith')


    review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer11)
    review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer3)
    review3 = Review(star_rating=7, restaurant=restaurant4, customer=customer4)
    review4= Review(star_rating=6, restaurant=restaurant6, customer=customer5)
    review5 = Review(star_rating=2, restaurant=restaurant8, customer=customer6)
    review6 = Review(star_rating=9, restaurant=restaurant3, customer=customer7)
    review7 = Review(star_rating=1, restaurant=restaurant1, customer=customer8)
    review8 = Review(star_rating=9, restaurant=restaurant7, customer=customer12)
    

    # Adding instances to the session
    session.add_all([restaurant1, restaurant2,restaurant3, restaurant4,restaurant5, restaurant6,restaurant7, restaurant8, customer1, customer2, customer3, customer7, customer5, customer6, customer7, customer8, customer9, customer10, customer11, customer12,review1, review2,review3, review4,review5, review6,review7, review8])

    # Committing changes
    session.commit()

