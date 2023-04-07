from flask import Flask, render_template
from users import users

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# The "@" decorator associates this route with the function immediately following
@app.route('/')          
def table():
    return render_template('index.html', users=users)






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.