USER_NAME = 'user_name'
EMAIL = 'email'
PASSWORD = 'password'
RECOVERY_KEYS = 'recovery_pkeys'
SECRET_QUESTIONS = 'secret_questions'
TWO_STEP_VERIFICATION = 'two_step_verification'
TWO_STEP_VERIFICATION_NUMBER = 'two_step_verification_number'
USER_LINK = 'user_link'

def createUser(name, email, password):
	user = dict()
	user[USER_NAME] = name
	user[EMAIL] = email
	user[PASSWORD] = password
	user[RECOVERY_KEYS] = list()
	user[SECRET_QUESTIONS] = list() # of tuples(q, a)
	user[TWO_STEP_VERIFICATION] = False
	user[TWO_STEP_VERIFICATION_NUMBER] = None
	user[USER_LINK] = None

	return user

def getEmail(user):
	return user.get(EMAIL)

def setEmail(user, newEmail):
	user[EMAIL] = newEmail

def getPassword(user):
	return user.get(PASSWORD)

def setPassword(user, newPassword):
	user[PASSWORD] = newPassword

