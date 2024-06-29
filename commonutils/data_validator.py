from werkzeug.exceptions import BadRequest
class Validator:
    def mandatory(self,**kwargs):
        for key,value in kwargs.items():
            if value is None or value =="" or value == "None" or value==[]:
                raise BadRequest(f'Required Field: {key}')
