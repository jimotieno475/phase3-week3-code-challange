from sqlalchemy import Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    reviews = relationship('Review', back_populates='restaurant')
    
    def __repr__(self):
        return f'Restaurant(id={self.id},'+\
            f'name={self.name},'+\
            f'price={self.price})'

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', back_populates='customer')

    def __repr__(self):
        return f'Customer(id={self.id},'+\
            f'first_name={self.first_name},'+\
            f'last_name={self.last_name})'
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f'Review(id={self.id},'+\
            f'star_rating={self.star_rating})'
