class User():
    """User class"""

    def __init__(self, user_name, email, password):
        """initializes the User object.
        Input:
            None
        Output:
            None
        Raises:
            None
        """
        self._user_name = user_name
        self._email = email
        self._password = password
        self._recovery_keys = set()
        self._secret_questions = set() # of tuples(q, a)
        self._two_step_verification = False
        self._two_step_verification_number = None
        self._user_link = None

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
    	self._user_name = value

    @user_name.deleter
    def user_name(self):
    	del self._user_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
    	self._email = value

    @email.deleter
    def email(self):
    	del self._email
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
    	self._password = value

    @password.deleter
    def password(self):
    	del self._password
    
    @property
    def recovery_keys(self):
        return self._recovery_keys

    @recovery_keys.setter
    def recovery_keys(self, value):
    	self._recovery_keys = value

    @recovery_keys.deleter
    def recovery_keys(self):
    	del self._recovery_keys
    
    @property
    def secret_questions(self):
        return self._secret_questions

    @secret_questions.setter
    def secret_questions(self, value):
    	self._secret_questions = value

    @secret_questions.deleter
    def secret_questions(self):
    	del self._secret_questions
    
    @property
    def two_step_verification(self):
        return self._two_step_verification

    @two_step_verification.setter
    def two_step_verification(self, value):
    	self._two_step_verification = value

    @two_step_verification.deleter
    def two_step_verification(self):
    	del self._two_step_verification
    
    @property
    def two_step_verification_number(self):
        return self._two_step_verification_number

    @two_step_verification_number.setter
    def two_step_verification_number(self, value):
    	self._two_step_verification_number = value

    @two_step_verification_number.deleter
    def two_step_verification_number(self):
    	del self._two_step_verification_number
    
    @property
    def user_link(self):
        return self._user_link

    @user_link.setter
    def user_link(self, value):
    	self._user_link = value

    @user_link.deleter
    def user_link(self):
    	del self._user_link

    def add_recovery_key(self, key):
    	self._recovery_keys.add(key)

    def remove_recovery_key(self, key):
    	self._recovery_keys.discard(key)

    def reset_recovery_keys(self):
    	self._recovery_keys.clear()

    def add_secret_question(self, question, answer):
    	self._secret_questions.add((question, answer))

    def remove_secret_question(self, question, answer):
    	self._secret_questions.discard((question, answer))
    	
    def reset_secret_questions(self):
    	self._secret_questions.clear()

def get_user_from_dict(data_dict):
	user = User(user_name=None, email=None, password=None)
	user.__dict__.update(data_dict)
	return user

def get_dict_from_user(user):
	return user.__dict__
