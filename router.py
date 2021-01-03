from flask_restful import Resource, request

post_endpoints = [
    '/list/users/posts',
    '/insert/user/post',
    '/list/user/post'
    '/profile',
    '/delete/user/post',
    '/delete/post',
    '/update/user/post',
    '/update/post'
]
user_endpoints = [
    '/list/users',
    '/cadastro',
    '/delete/user',
    '/update/user'
]
auth_endpoints = ['/login','/logout']


class Post(Resource):
    def post(self):
        pass
    def get(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass

class User(Resource):
    def post(self):
        pass
    def get(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass


class Auth(Resource):
    def post(self):
        if '/login' in request.path:
            pass

        if '/logout' in request.path:
            pass