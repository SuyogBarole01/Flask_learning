from app import app

@app.route('/pcat/added')
def added():
    return 'Product category added'