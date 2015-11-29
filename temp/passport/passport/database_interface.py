"""Contains Database class and methods for serialization"""

class Database():
    """Database class containing methods for manipulating data in the db"""

    def __init__(self):
        """initializes the db object.
        Input:
            None
        Output:
            None
        Raises:
            None
        """
        self.services = dict() # services:(tags, {user:blob})
        self.tags = set()

    def add_service(self, service, tags):
        """Add a new service to the database
        Input:
            service: string
            tags: string comma separated in case of multiple
        Output:
            None
        Raises:
            ValueError: if adding service that already exists
        """
        if service not in self.services:
            tags = set(tags.split(','))
            self.services[service] = (tags, dict())
            self.tags = self.tags | tags
        else:
            raise ValueError("Trying to add service that already exists")

    def remove_service(self, service):
        """Removes a service from the database
        Input:
            service: string
        Output:
            None
        Raises:
            ValueError: if removing a service that doesnt exist
        """
        if service in self.services:
            del self.services[service]
            self._update_global_tags()
        else:
            raise ValueError("Trying to remove a service that doesnt exist")

    def update_service_tags(self, service, tags):
        """Updates service tags
        Input:
            service: string
            tags: string comma separated in case of multiple
        Output:
            None
        Raises:
            ValueError: if updating tags of service that doesnt exist
        """
        if service in  self.services:
            self.services[service][0] = tags
            self._update_global_tags()
        else:
            raise ValueError("Trying to update tags of service that doesnt exist")

    def _update_global_tags(self):
        """Updates global tags upon deletion of a service.
        Input:
            None
        Output:
            None
        Raises:
            None
        """
        self.tags = set()
        for service in self.services.keys():
            service_tags = self.services[service][0]
            self.tags = self.tags | service_tags

    def insert_user(self, service, user, blob):
        """Inserts record into database
        Input:
            service: string
            user: string
            tags: string comma separated in case of multiple
            blob: string
        Output:
            None
        Raises:
            ValueError: if service doesnt exist
                        or inserting service:user combination that already exists
        """
        if service not in self.services:
            raise ValueError("Trying to add user to unknown service")

        if user in self.services[service][1]:
            raise ValueError("Trying to insert service:user combination that already exists")

        self.services[service][1][user] = blob

    def remove_user(self, service, user):
        """Removes record from database
        Input:
            service: string
            user: string
        Output:
            None
        Raises:
            ValueError: if removing service:user combination that doesnt exist
        """
        if service in self.services and user in self.services[service][1]:
            del self.services[service][1][user]
        else:
            raise ValueError("Trying to remove service:user combination that doesnt exist")

    def update_user(self, service, user, blob):
        """Updates record in database
        Input:
            service: string
            user: string
            tags: string comma separated in case of multiple
            blob: string
        Output:
            None
        Raises:
            ValueError: if updating service:user combination that doesnt exist
        """
        if service in self.services and user in self.services[service][1]:
            self.services[service][1][user] = blob
        else:
            raise ValueError("Trying to update service:user combination that doesnt exist")

    def get_services(self):
        """Get services in database
        Input:
            None
        Output:
            dict_list
        Raises:
            None
        """
        return self.services.keys()

    def get_tags(self):
        """Get tags
        Input:
            None
        Output:
            set
        Raises:
            None
        """
        return self.tags

    def get_users(self, service=None):
        """Get users
        Input:
            service (optional): string containing service name
        Output:
            set containing users
        Raises:
            ValueError: if trying to get users of unknown service
        """
        users = set()
        if service:
            try:
                service_users = self._get_service_users(service)
                users = users | set(service_users)
            except ValueError:
                raise
        else:
            for key in self.services.keys():
                service_users = self._get_service_users(key)
                users = users | set(service_users)

    def _get_service_users(self, service):
        """Get users of a service
        Input:
            service: string containing service name
        Output:
            set containing users
        Raises:
            ValueError: if trying to get users of unknown service
        """
        if service in self.services:
            return self.services[service][1].keys()
        else:
            raise ValueError("trying to get users of unknown service")

    def get_data(self, service, user):
        """Get Data of service:user combination
        Input:
            service: string containing service name
            user: string containing service user
        Output:
            string
        Raises:
            ValueError: if trying to get data of unknown service:user combination
        """
        if service in self.services and user in self.services[service][1]:
            return self.services[service][1][user]
        else:
            raise ValueError("Trying to get data of unknown service:user combination")

    def search_by_tag(self, tag):
        """Search for services with the given tag
        Input:
            tag: string containing tag
        Output:
            list of services
        Raises:
            None
        """
        tag = set([tag])
        matched = []
        if tag and self.tags.intersection(tag):
            for key, value in self.services.items():
                service_tags = value[0]
                if service_tags.intersection(tag):
                    matched.append(key)
        return matched

    def search_by_user(self, user):
        """Search for services with the given user
        Input:
            tag: string containing tag
        Output:
            list of services
        Raises:
            None
        """
        tag = set([user])
        matched = []
        if tag:
            for key, value in self.services.items():
                service_users = value[1].keys()
                for service_user in service_users:
                    if service_user == user:
                        matched.append(key)
                        break
        return matched


#def load(data):
#    """Loads the databse """
#    data = None
#    return data
#
#def serialize(database):
#    """Converts the database object into string
#    Input:
#        tag: string containing tag
#    Output:
#        list of services
#    Raises:
#        None
#    """
#    database = None
#    return database
