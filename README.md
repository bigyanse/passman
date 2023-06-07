# passman

PassMan, a password manager based upon Django Project with login, one time registration, logout, password saving functionality.

## Project objective
1) Login, registration functionality with default django user model
2) Restriction to views without login
3) One time registration and single user application
4) Using django secure hashing encryption for passwords
5) Password saving, editing and deleting functionality

## How to install?
1) Clone this repo in your local machine, using `git clone ...`
2) Get inside `passman` directory
3) Initialize the virtual environment in this directory by `python -m venv .`. Note: Use Python3
4) Then `source bin/activate`
5) `pip install -r requirements.txt`
6) `cd src`
7) `python manage.py runserver`
8) `http://127.0.0.1:8000/`

## Login Details
Currently, a user is on the database. You can delete it with django administration and create new one. The registration is a one time process. The login details is same with the django administration too.

Username: `admin`
Password: `admin`

## Screenshot
<div>
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/b3dc29e7-39ec-46ef-9461-40a6b8925a87" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/63a72696-53fb-429a-8af0-4b1ac38c7d63" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/5525141e-daaf-4006-b4d5-3d6588ab06fe" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/66808bac-6043-4c91-980a-efd1a246bfdb" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/2d3c21c4-6e16-4811-8b42-3ab58fd8ae73" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/e2f4ca96-9a47-44a7-9450-57aecef849d5" width="200">
	<img align=top src="https://github.com/bigyanse/passman/assets/134137654/78581bed-1da5-4dc0-953c-cccaffd267d1" width="200">
</div>
