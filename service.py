class Service():
    """Service class"""

    def __init__(self, name, tags, users):
        """initializes the service object.
        Input:
            None
        Output:
            None
        Raises:
            None
        """
        self._name = name
        self._tags = tags
        self._users = users

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
    	self._name = value

    @name.deleter
    def name(self):
    	del self._name

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
    	self._tags = value

    @tags.deleter
    def tags(self):
    	del self._tags

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
    	self._users = value

    @users.deleter
    def users(self):
    	del self._users
    
    def add_tag(self, tag):
    	self._tags.add(tag)

    def remove_tag(self, tag):
    	self._tags.discard(tag)

    def reset_tags(self):
    	self._tags.clear()

    def add_user(self, name, data):
    	if name in self._users:
    		raise KeyError("Adding user that already exists")
    	self._users[name] = data

    def remove_user(self, name):
    	if name not in self._users:
    		raise KeyError("Removing user that does not exists")
    	self._users.pop(name)
    	
    def update_user(self, name, data):
    	if name not in self._users:
    		raise KeyError("updating user that does not exists")
    	self._users[name] = data

    def reset_user(self):
    	self._users.clear()

    def get_user_data(self, name):
    	if name not in self._users:
    		raise KeyError("Retrieving data of user that does not exists")
    	return self._users[name]

    def print_pretty_string(self, outstream):
    	print('----------{}----------'.format(self._name), file=outstream)
    	print('Tags: ', end=' ')
    	print(*self._tags, sep=',', file=outstream)
    	print('Users:', file=outstream)
    	for key, value in self._users.items():
	    	print('\t{} : {}'.format(key, value), file=outstream)
    	print('----------------------', file=outstream)

def get_service_from_dict(data_dict):
	service = Service(name=None, tags=set(), users=dict())
	service.__dict__.update(data_dict)
	return service

def get_dict_from_service(service):
	return service.__dict__
