import json
from flask import request
from modules.users.utils.http_response import *
from modules.users.utils.validators import Validators
from modules.users.utils.formats import Formats
from modules.users.models.UsersModel import UserModel

class UserController:

    def getUserByName():
        """
        file: ../swagger/getUserByName.yaml
        """
        try:
            data = request.args
            errors = []
            val = Validators()
            form = Formats()
            if "name" in data:
                if not val.isNotEmptyString(data['name'], 4):
                    errors.append('O campo "name" está invalido')
            else:
                errors.append('O campo "name" e requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            user = UserModel.objects(name=data['name']).first()
            if not user:
                return forbidden()
            
            return success_200(user.to_dict())
        except:
            return internalError()

    def getUserByIlike():
        """
        file: ../swagger/getUserByIlike.yaml
        """
        try:
            data = request.args
            errors = []
            val = Validators()
            form = Formats()
            if "name" in data:
                if not val.isNotEmptyString(data['name'], 3):
                    errors.append('O campo "name" está invalido')
            else:
                errors.append('O campo "name" e requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            users = UserModel.objects(name__icontains=data['name'])
            if not users:
                return forbidden()
            ret = []
            for user in users:
                ret.append(user.to_dict())

            return success_200(ret)
        except:
            return internalError()

    def getUserByDocument():
        """
        file: ../swagger/getUserByDocument.yaml
        """
        try:
            data = request.args
            errors = []
            val = Validators()
            form = Formats()
            if "document" in data:
                if not val.isNotEmptyString(data['document'], 6):
                    errors.append('O campo "document" está invalido')
            else:
                errors.append('O campo "document" e requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            user = UserModel.objects(document=data['document']).first()
            if not user:
                return forbidden()
            
            return success_200(user.to_dict())
        except:
            return internalError()
        

    def cadastraUser():
        """
        file: ../swagger/cadastraUser.yaml
        """
        try:
            data = json.loads(request.data)
            errors = []
            val = Validators()
            if "name" in data:
                if not val.isNotEmptyString(data['name'], 4):
                    errors.append('O campo "name" está invalido')
            else:
                errors.append('O campo "name" é requerido.')

            if "document" in data:
                if not val.isNotEmptyString(data['document'], 6):
                    errors.append('O campo "document" está invalido')
            else:
                errors.append('O campo "document" é requerido.')
            
            if "address" in data:
                if not val.isNotEmptyString(data['address'], 6):
                    errors.append('O campo "address" está invalido')
            else:
                errors.append('O campo "address" é requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            newUser = UserModel(name=data['name'],
                document=data['document'],
                address=data['address']
            )

            newUser.save()
            return success_201()
        except:
            return internalError()


    def editaUser():
        """
        file: ../swagger/editaUser.yaml
        """
        try:
            data = json.loads(request.data)
            errors = []
            val = Validators()
            if "document" in data:
                if not val.isNotEmptyString(data['document'], 6):
                    errors.append('O campo "document" está invalido')
            else:
                errors.append('O campo "document" é requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            user = UserModel.objects(document=data['document']).first()
            if not user:
                return forbidden()
            
            if "name" in data:
                if not val.isNotEmptyString(data['name'], 4):
                    errors.append('O campo "name" está invalido')
                else:
                    user.update(name=data['name'])

            if "address" in data:
                if not val.isNotEmptyString(data['address'], 6):
                    errors.append('O campo "address" está invalido')
                else:
                    user.update(address=data['address'])  
            if len(errors) > 0:
                return bad_request(errors)
            user.save()
            return success_201()

        except:
            return internalError()


    def deletaUser():
        """
        file: ../swagger/deletaUser.yaml
        """
        try:
            data = json.loads(request.data)
            errors = []
            val = Validators()
            if "document" in data:
                if not val.isNotEmptyString(data['document'], 6):
                    errors.append('O campo "document" está invalido')
            else:
                errors.append('O campo "document" é requerido.')

            if len(errors) > 0:
                return bad_request(errors)

            user = UserModel.objects(document=data['document']).first()
            if not user:
                return forbidden()

            user.delete()
            return success_200("Registro deletado com sucesso")
        except:
            return internalError()