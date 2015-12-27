import service
import copy

class Data_Manager():

    def __init__(self):
        self.services = dict() # name:service where service is tags, {user:blob}
        self.tags = set()
        self.users = set()

    def add_service(self, service):
        if service.name in self.services:
            raise ValueError("Trying to add service that already exists")
        tags = service.tags
        self.services[service.name] = service
        self.tags = self.tags | tags
        self.users = self.users | service.users.keys()

    def remove_service(self, service):
        if service.name not in self.services:
            raise ValueError("Trying to remove a service that doesnt exist")
        self.services.pop(service.name)
        self._update_tags()
        self._update_users()

    def update_service(self, service):
        if service.name not in self.services:
            raise ValueError("Trying to modify a service that doesnt exist") 
        self.services[service.name] = service
        self._update_tags()
        self._update_users()
            
    def get_service(self, name):
        if name not in self.services:
            raise ValueError("Trying to retrieve a service that doesnt exist")
        return self.services[name]

    def _update_tags(self):
        self.tags = set()
        for service in self.services.values():
            self.tags = self.tags | service.tags

    def _update_users(self):
        self.users = set()
        for service in self.services.values():
            self.users = self.users | service.users.keys()

    def update_tags_and_users(self):
        self._update_users()
        self._update_tags()

    # def insert_user(self, service_name, user_name, data):
    #     if service_name not in self.services:
    #         raise ValueError("Trying to add user to unknown service")
    #     service = self.services[service_name]
    #     service.add_user(user_name, data)
    #     self.users.add(user_name)

    # def remove_user(self, service_name, user_name):
    #     if service_name not in self.services:
    #         raise ValueError("Trying to remove user from unknown service")
    #     service = self.services[service_name]
    #     service.remove_user(user_name)
    #     self._update_users()

    # def update_user(self, service_name, user_name, data):
    #     if service_name not in self.services:
    #         raise ValueError("Trying to update user in unknown service")
    #     service = self.services[service_name]
    #     service.update_user(user_name, data)
    #     self._update_users()

    # def get_users(self, service_name=None):
    #     users = set()
    #     if service_name:
    #         service = self.services[service_name]
    #         users = set(service.users.keys())
    #     else:
    #         users = self.users
    #     return users

    # def get_data(self, service_name, user_name):
    #     if service_name not in self.services:
    #         raise ValueError("Trying to retrieve data of user in unknown service")
    #     service = self.services[service_name]
    #     return service.get_user_data(user_name)

    def find_services_with_tag(self, tag):
        matched = []
        if tag in self.tags:
            for service_name, service in self.services.items():
                service_tags = service.tags
                if tag in service_tags:
                    matched.append(key)
        return matched

    def find_services_with_user(self, user_name):
        matched = []
        if user_name in self.users:
            for service_name, service in self.services.items():
                service_users = set(service.users.keys())
                if user_name in service_users:
                    matched.append(key)
        return matched

def get_manager_from_dict(data_dict):
    manager = Data_Manager()
    manager.__dict__.update(copy.deepcopy(data_dict))
    for key, value in manager.services.items():
        manager.services[key] = service.get_service_from_dict(value)
    return manager

def get_dict_from_manager(manager):
    data_dict = copy.deepcopy(manager.__dict__)
    services = data_dict['services']
    for key, value in services.items():
        services[key] = service.get_dict_from_service(value)
    return data_dict
