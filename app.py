from flask import Flask, render_template
#import for the blueprint address
from bluePrints.address.addressBP import address

#Instance of the FlaskApp
app = Flask(__name__)

#Register of the blueprint for the calculus of address
app.register_blueprint(address)

#Adding two routes for initial page, in this page (index.html), i described the problem
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

#For page not found error control
@app.errorhandler(404)
def error_not_found(e):
    return render_template('404.html'),404

#For internal server error control
@app.errorhandler(500)
def error_internal_server(e):
    return render_template('500.html'),500


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 