# services dict {tags:set of tags, users:dict of users}
# tags set of strings
# users in services dict {name:blob}
# user 

# services
# {
# 	tags (set): tag1, tag2, tag3,
# 	users (dict):{
# 		username1:blob,
# 		username2:blob
# 	}
# }

# blob
# {
# 	password: password,
# 	email: email,
# 	2step-Verification:2step-Verification,
# 	secret questions: array{
# 		(question1, answer1),
# 		(question2, answer2)
# 	}
# 	link:link,
# 	recoveryKey:array{
# 		key1,
# 		key2, 
# 	}
# }

#for services
TAGS = 'tags'
USERS = 'users'

#for users
PASSWORD = 'password'
EMAIL = 'email'
TWO_STEP_VERIFICATION = 'two_step_verification'
SECRET_QUESTIONS = 'secret_questions'
USER_LINK = 'user_link'
RECOVERY_KEYS = 'recovery_pkeys'
