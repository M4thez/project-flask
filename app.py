from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    isCompleted = db.Column(db.Boolean, default=False)


@app.route('/')
def index():
    todoList = Todo.query.all()
    return render_template('index.html', todoList=todoList)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todoID>')
def delete(todoID):
    todo = Todo.query.filter_by(id=todoID).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<int:todoID>')
def complete(todoID):
    todo = Todo.query.filter_by(id=todoID).first()
    todo.isCompleted = not todo.isCompleted
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
