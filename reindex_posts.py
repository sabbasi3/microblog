from app import create_app, db
from app.models import Post
from app.search import add_to_index

app = create_app()
with app.app_context():
    for post in db.session.scalars(db.select(Post)):
        add_to_index('post', post)
    print("All posts have been re-indexed.")