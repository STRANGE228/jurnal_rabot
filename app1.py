from flask import Flask, render_template
from data.__all_models import User, Jobs
from data import db_session

app = Flask(__name__)


@app.route('/')
def table():
    with db_session.create_session() as db_sess:
        users = db_sess.query(User).all()
        colonisters = dict()
        for user in users:
            colonisters[user.id] = f"{user.name} {user.surname}"
        jobs = db_sess.query(Jobs).all()
    return render_template('works_log.html', jobs=jobs, users=colonisters)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(host='localhost', port=8080, debug=True)
