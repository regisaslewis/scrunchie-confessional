from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, metadata

product_owners = db.Table(
    "products_owners",
    metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True)
)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    hairstyle = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))

    group = db.relationship("Group", back_populates="members")
    products = db.relationship("Product", secondary=product_owners, back_populates="owners")

    def __repr__(self):
        return f"User# {self.id}: {self.username}"

class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    condition = db.Column(db.Integer)
    is_new = db.Column(db.Boolean, default=False, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))

    brand = db.relationship("Brand", back_populates="products")
    owners = db.relationship("User", secondary=product_owners, back_populates="products")


    def __repr__(self):
        return f"Product# {self.id}: {self.name}"
    
class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    members = db.relationship("User", back_populates="group", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Group #{self.id}: {self.name} | {('Members: ', self.members) if self.members else 'No current members'}"
    
class Brand(db.Model, SerializerMixin):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    products = db.relationship("Product", back_populates="brand", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Brand #{self.id}: {self.name}{(' | Products: ', self.products) if self.products else ''}"


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.Column(db.String)