# Password-Strength-Checker-Flask

A simple web application built with Flask that evaluates the strength of user passwords and suggests improvements. The application checks various criteria to determine password strength and provides feedback to users.

## Features

- Evaluates password strength based on length, character variety (uppercase, lowercase, digits, special characters).
- Provides feedback on whether the password is Weak, Okay, Good, or Strong.
- User-friendly interface for easy interaction.

## Technologies Used

 Python: The programming language used for backend development.
 Flask: A lightweight web framework for building web applications.
 HTML/CSS: For creating the frontend user interface.
 Regular Expressions: For validating password criteria.

 ## Installation

  -Prerequisites
    Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

     
  -Steps to Install
  1. Clone the Repository
     `git clone [](https://github.com/Joe6001/Password-Strength-Checker-Flask/)`
     
     `cd Password_Strength_Checker-Flask`
  3. Create a virtual environment(optional but recommended):
     `python -m venv "any-name-you-want"`
     
     `source venv/bin/activate`
     
     `On Windows use venv\Scripts\activate`
  5. Install Flask
     `pip install flask`
  6. Run the Applicatiom
     `python app.py` 
  7. Access the application
      `Open your web browser and go to `http://127.0.0.1:5000`.`

## Usage

1. Enter a password in the input field.
2. Click the "Check Strength" button.
3. The application will display the strength of your password based on predefined criteria.

## Code Overview

The main logic for evaluating password strength is implemented in the `password_strength` function, which checks for:

- Minimum length (8 characters)
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of digits
- Presence of special characters

The function returns a score that determines the strength category of the password.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask community for providing a robust framework for web development.
