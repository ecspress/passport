# USER_NAME = 'user_name'
# EMAIL = 'email'
# PASSWORD = 'password'
# RECOVERY_KEYS = 'recovery_keys'
# SECRET_QUESTIONS = 'secret_questions'
# TWO_STEP_VERIFICATION = 'two_step_verification'
# TWO_STEP_VERIFICATION_NUMBER = 'two_step_verification_number'
# USER_LINK = 'user_link'

class User():
    """User class"""

    def __init__(self, user_name=None, email=None, password=None):
        """initializes the User object.
        Input:
            None
        Output:
            None
        Raises:
            None
        """
        self._userName = user_name
        self._email = email
        self._password = password
        self._recoverKeys = list()
        self._secretQuestions = list() # of tuples(q, a)
        self._twoStepVerification = False
        self._twoStepVerificationNumber = None
        self._userLink = None

#     def getUserAsDict(self):
#     	data = dict()
#     	data[EMAIL] = self._email
#     	data[PASSWORD] = self._password
#     	data[RECOVERY_KEYS] = self._recoverKeys
#     	data[SECRET_QUESTIONS] = self._secretQuestions
#     	data[TWO_STEP_VERIFICATION] = self._twoStepVerification
#     	data[TWO_STEP_VERIFICATION_NUMBER] = self._twoStepVerificationNumber
#     	data[USER_LINK] = self._userLink
#     	return self._name, data

def getUserFromDict(dict):
	user = User()
	user.__dict__.update(dict)
	return user

def getDictFromUser(user):
	return user.__dict__

# def getUserFromDict(name, data_dict):
# 	user = User(name, data_dict[EMAIL], data_dict[PASSWORD])
# 	user.setRecoveryKeys(data_dict[RECOVERY_KEYS])
# 	user.setSecretQuestions(data_dict[SECRET_QUESTIONS])
# 	user.setTwoStepVerification(data_dict[TWO_STEP_VERIFICATION])
# 	user.setTwoStepVerificationNumber(data_dict[TWO_STEP_VERIFICATION_NUMBER])
# 	user.setUserLink(data_dict[USER_LINK])
# 	return user

# def getEmail(user):
# 	return user.get(EMAIL)

# def setEmail(user, newEmail):
# 	user[EMAIL] = newEmail

# def getPassword(user):
# 	return user.get(PASSWORD)

# def setPassword(user, newPassword):
# 	user[PASSWORD] = newPassword

