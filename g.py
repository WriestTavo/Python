clients = [{'name': 'Pablo', 'company': 'Google', 'email': ' pablo@google.com ', 'position': 'Software engineer'},

{
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricado@facebook.com',
    'position': 'Data engineer'
},
]

def create_client (cliente): clientes globales

if client not in clients :
    clients.append(client)
else:
    print('Clients is not  in clients list')
def list_clients (): print ('uid | name | company | email | position') print ('*' * 50)

for idx, client in enumerate(clients):
    print("{uid}| {name} | {company} | {email} | {position}".format(
        uid=idx,
        name=client['name'],
        company=client['company'],
        email=client['email'],
        position=client['position']))
def update_client (client_id, update_client): clientes globales 

if len(clients) -1 >= client_id:
    clients[client_id] = update_client
else:
    print('client is not in clients list')
def delete_client (client_id): clientes globales

for idx, client in enumerate(client):
    if idx == client_id:
        del clients[idx]
        break
def search_client (client_name):

for client in clients:
    if client ['name'] != client_name:
        continue
    else:
        return True
def _get_client_field (field_name, message = '¿Qué es los clientes {}'): campo = Ninguno

while not field:
    field = input('What is the client {}?'.format(field_name))

return field
def _get_client_name (): client_name = None

while not client_name:
    client_name = str.lower(input('what is the client name?'))

    if client_name == 'exit':
        client_name = None
        break

return client_name
def _print_welcome (): print (' ' * 50) print (' Welcome to ventas *') print (' ' * 50) print ('¿qué le gustaría hacer hoy?') print ('[C] reate client' ) print ('[L] ist clients') print ('[U] pdate client') print ('[D] elete client') print ('[S] earch client') print ('')

if name == ' main ': _print_welcome ()

command = input()
command = command.upper()

if command == 'C':
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    create_client(client)
    list_clients()
elif command == 'L':
    list_clients()
elif command == 'U':
    client_name = _get_client_name()
    update_client_name = input('What is updated cliend  name: ')

    update_client(client_name, update_client_name)
    list_clients()
elif command == 'D':
    client_name = _get_client_name()
    delete_client(client_name)
    list_clients()
elif command == 'S':
    client_name = _get_client_name()
    found = search_client(client_name)

    if found:
        print('The client is in the clients list')
    else:
        print('The client: {} is not in our clients list'. format(client_name))
else:
    print('Invalid command')