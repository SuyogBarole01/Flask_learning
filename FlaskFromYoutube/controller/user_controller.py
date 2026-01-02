from app import app

@app.route('/user/signup')
def signup():
    return 'Signup page created'