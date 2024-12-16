from flask import Flask, request, render_template # Import necessary modules from Flask
import re # Import the regular expression module

# Create an instance of the Flask class
app = Flask(__name__)

def password_strength(password):
	score = 0 # Initialize score to 0
	length = len(password) # Get the length of the password

	# Check for minimum length requirement
	if length <8:
		return "Weak", score # Return "Weak" if password is shorter than 8 characters

	# Increment score for longer passwords
	if length >12:
		score+= 1

	# Check for uppercase letters and increment score if found
	if re.search(r'[A-Z]', password):
		score+= 1

	# Check for lowercase letters and increment score if found
	if re.search(r'[a-z]', password):
		score+= 1

	# Check for digits and increment if found
	if re.search(r'/d', password):
		score+= 1

	# Check for special characters and increment if found
	if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
		score+= 1

	# Determine strength based on the final score
	if score<3:
		return "Weak", score
	if score==3:
		return "Okay", score
	if score<5:
		return "Good", score
	else:
		 return "Strong", score

@app.route('/', methods=['GET', 'POST'])  # Define the route for the root URL, and allow only GET and POST methods
def index():
	strength = ""  # Initialize strength variable to hold password strength feedback

	if request.method == 'POST': 	# Check if the request method is POST(form submission) 
		password = request.form['password']  # Retrieve the submitted password from the form
		strength, _ = password_strength(password)  # Evaluate the password strength

	# Render the index.html template, passing the strength feedback to it
	return render_template('index.html', strength=strength)
if __name__ == '__main__':
	app.run(debug=True) # Run the app in dubeg mode when the script is executed directly
