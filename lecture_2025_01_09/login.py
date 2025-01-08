def login(username, password):
    database = {
        'davnords': 'bluemarlin123',
        'johndoe': 'password123'
    }
    if username in database and database[username] == password:
        return True
    return False