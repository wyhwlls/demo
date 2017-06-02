from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'dv_product'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    long_name = db.Column(db.String(256))
    market_price = db.Column(db.Float)
    sell_price = db.Column(db.Float)
    # is_online = db.Column(db.Boolean, default=0)
    # cost_price = db.Column(db.Float, default=0)
    # gmt_created = db.Column(db.DateTime)
    # gmt_modified = db.Column(db.DateTime)
    # deleted = db.Column(db.Boolean, default=0)
    # sort = db.Column(db.Integer, default=99)
    # shelf_life = db.Column(db.Integer, nullable=False, default=180)
    # pre_shelf_life = db.Column(db.Integer, default=160)
    # product_img1 = db.Column(db.String(256), nullable=False)
    # product_img2 = db.Column(db.String(256))
    # product_img3 = db.Column(db.String(256))
    # product_img4 = db.Column(db.String(256))
    # unit = db.Column(db.String(32), nullable=False,)
    # country = db.Column(db.String(128))


    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()


@app.route('/')
def show_all():
    return render_template('show_all.html',
        todos=Todo.query.order_by(Todo.name.desc()).all()
    )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form[''], request.form['text'])
            todo = Todo(request.form['name'], request.form['text'])
            todo = Todo(request.form['long_name'], request.form['text'])
            todo = Todo(request.form['market_price'], request.form['text'])
            todo = Todo(request.form['sell_price'], request.form['text'])
            # todo = Todo(request.form['is_online'], request.form['text'])
            # todo = Todo(request.form['cost_price'], request.form['text'])
            # todo = Todo(request.form['gmt_created'], request.form[''])
            # todo = Todo(request.form['gmt_modified'], request.form[''])
            # todo = Todo(request.form['deleted'], request.form['text'])
            # todo = Todo(request.form['sort'], request.form['text'])
            # todo = Todo(request.form['shelf_life'], request.form['text'])
            # todo = Todo(request.form['pre_shelf_life'], request.form['text'])
            # todo = Todo(request.form['product_img1'], request.form['text'])
            # todo = Todo(request.form['product_img2'], request.form['text'])
            # todo = Todo(request.form['product_img3'], request.form['text'])
            # todo = Todo(request.form['product_img4'], request.form['text'])
            # todo = Todo(request.form['unit'], request.form['text'])
            # todo = Todo(request.form['country'], request.form['text'])

            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    app.run()
