from charIO import _Getch
import copy
import data_manager
import os
import service
import sys
import user
import util

file_name = None
manager = None

#TODO: STOP USING EVAL, USE AST.LITERAL_EVAL BY FINDING SOLUTION FOR SET(), POSSIBLY BY USING JSON.DUMPS

def read_manager_from_file():
	global manager
	data_bytes = util.read_file_bytes(file_name)
	data_dict = eval(data_bytes.decode())
	manager = data_manager.get_manager_from_dict(data_dict)

def save_manager_to_file(create_backup):
	data_dict = data_manager.get_dict_from_manager(manager)
	data_bytes = str(data_dict).encode()
	util.write_bytes_to_file(file_name, data_bytes)

def prompt_to_add_user_to_service(service_to_modify):
	global manager
	print("Please enter user name to add to {}".format(service_to_modify.name))
	user_name = input()
	new_user = user.User(user_name=user_name, email=None, password=None)
	service_to_modify.add_user(user_name, user.get_dict_from_user(new_user))
	# manager.update_service(service_to_modify)
	manager.update_tags_and_users()
	save_manager_to_file(True)

def prompt_to_delete_user_of_service(service_to_modify):
	global manager
	print("Please enter user name to remove from {}".format(service_to_modify.name))
	user_name = input()
	service_to_modify.remove_user(user_name)
	# manager.update_service(service_to_modify)
	manager.update_tags_and_users()
	save_manager_to_file(True)

def prompt_to_modify_user_of_service():
	print("promptToModifyUserOfAService")

def prompt_to_display_user_of_service(service_to_modify):
	print("Please enter user name of {} to view".format(service_to_modify.name))
	user_name = input()
	print(service_to_modify.get_user_data(user_name))

def list_all_service_users(service_to_modify):
	leader = '-----{}--users-----'.format(service_to_modify.name) 
	print(leader)
	print(*service_to_modify.users, sep=',')
	print(len(leader) * '-')

def process_user_menu_choice(input_char, service_to_modify):
	if input_char == 'a':
		prompt_to_add_user_to_service(service_to_modify)
	elif input_char == 'd':
		prompt_to_delete_user_of_service(service_to_modify)
	elif input_char == 'm':
		prompt_to_modify_user_of_service()
	elif input_char == 'v':
		prompt_to_display_user_of_service(service_to_modify)
	elif input_char == 'l':
		list_all_service_users(service_to_modify)
	elif input_char == 'b':
		pass
	else:
		display_wrong_input_alert(input_char)

def display_user_menu(service_to_modify):
	print("Please choose from the following options.")
	print("\t(a) to add user to {}".format(service_to_modify.name))
	print("\t(d) to delete user from {}".format(service_to_modify.name))
	print("\t(m) to modify user of {}".format(service_to_modify.name))
	print("\t(v) to view user of {}".format(service_to_modify.name))
	print("\t(l) to list all users of {}".format(service_to_modify.name))
	print("\t(b) to return")

def user_main(getch, input_char, service_to_modify):
	while input_char != 'b':
		display_user_menu(service_to_modify)
		input_char = getch()
		clear_screen()
		process_user_menu_choice(input_char, service_to_modify)

def prompt_for_service_modification(getch, input_char):
	print("Please enter service name/url to modify")
	service_name = input()
	service_to_modify = manager.get_service(service_name)
	# user_main(getch, input_char, copy.deepcopy(service_to_modify))
	user_main(getch, input_char, service_to_modify)

def prompt_for_service_addition():
	global manager
	print("Please enter service name/url to add")
	service_name = input()
	print("Please enter service tags separated by comma's")
	tags = input()
	tags = {x.strip() for x in tags.split(',')}
	service_to_add = service.Service(name=service_name, tags=tags, users=dict())
	manager.add_service(service_to_add)
	save_manager_to_file(True)

def prompt_for_service_deletion():
	print("Please enter service name/url to delete")
	service_name = input()
	service_to_delete = manager.get_service(service_name)
	manager.remove_service(service_to_delete)
	save_manager_to_file(True)

def prompt_to_display_service():
	print("Please enter service name/url to view")
	service_name = input()
	service_to_view = manager.get_service(service_name)
	service_to_view.print_pretty_string(sys.stdout)

def list_all_services():
	for service in manager.services.values():
		service.print_pretty_string(sys.stdout)

def list_all_tags():
	print('-----TAGS-----')
	print(*manager.tags, sep=',')
	print('--------------')

def list_all_users():
	print('-----USERS-----')
	print(*manager.users, sep=',')
	print('---------------')

def process_service_menu_choice(getch, input_char):
	if input_char == 'a':
		prompt_for_service_addition()
	elif input_char == 'd':
		prompt_for_service_deletion()
	elif input_char == 'm':
		prompt_for_service_modification(getch, input_char)
	elif input_char == 'v':
		prompt_to_display_service()
	elif input_char == 'l':
		list_all_services()
	elif input_char == 't':
		list_all_tags()
	elif input_char == 'u':
		list_all_users()
	elif input_char == 'q':
		pass
	else:
		display_wrong_input_alert(input_char)

def display_service_menu():
	print("Please choose from the following options.")
	print("\t(a) to add service")
	print("\t(d) to delete service")
	print("\t(m) to modify service")
	print("\t(v) to view service")
	print("\t(l) to list all services")
	print("\t(t) to list all tags")
	print("\t(u) to list all users")
	print("\t(q) to quit")

def service_main(getch, input_char):
	while input_char != 'q':
		display_service_menu()
		input_char = getch()
		clear_screen()
		process_service_menu_choice(getch, input_char)

def display_wrong_input_alert(input_char):
	print("invalid option ({}) selected.".format(input_char))

def show_welcome_screen():
	print("Welcome to digital airport. Please choose from the following options.")
	print("\t(e) if you already have a passport file")
	print("\t(n) to create a new passport file")
	print("\t(q) to quit")

def process_welcome_screen_input(input_char):
	global file_name
	global manager
	if input_char == 'e':
		print("Please enter the file path")
		file_name = input()
		read_manager_from_file()
		print("read file at {}".format(file_name))
	elif input_char == 'n':
		print("Please enter the file path")
		file_name = input()
		print("file will be created at {}".format(file_name))
		manager = data_manager.Data_Manager()
		save_manager_to_file(False)
	elif input_char == 'q':
		pass
	else:
		display_wrong_input_alert(input_char)

def clear_screen():
	os.system('clear')
	#os.system('cls')

def main(getch):
	clear_screen()
	input_char = ''
	while input_char != 'q':
		show_welcome_screen()
		input_char = getch()
		clear_screen()
		process_welcome_screen_input(input_char)
		if(file_name):
			break
	if(file_name):
		service_main(getch, input_char)

if __name__ == "__main__":
	getch = _Getch()
	main(getch)
