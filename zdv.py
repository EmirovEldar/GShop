from app import db, Article, app

with app.app_context():
    db.create_all()