from app.models.user_model import User
from app.extensions import db


def get_all_users():
    """
    Returns every existing user
    """

    return User.query.all()


def create_user(user_data):
    """
    Create new user
    """
    new_user = User(
        name=user_data['name'],
        email=user_data['email'],
    )
    new_user.set_password(user_data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user


def init_db():
    """
    Create admin user, if it doesn't already exist.
    """
    user = User(name="Admin", email="admin@example.com")
    user.set_password("password")

    if not db.session.query(User).filter_by(email=user.email).first():
        print("User admin created.")
        db.session.add(user)
        db.session.commit()
    else:
        print("User exists.")