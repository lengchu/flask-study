from app import route

@route('/user', methods = ['GET'])
def findUser(): 
    return '<h1>user</user>'
