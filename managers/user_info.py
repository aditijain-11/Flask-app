from commonutils import Validator
class UserInfo:
    @classmethod
    async def create_user(self, data: dict) -> dict:
        name = data["name"]
        email = data["email"]
        mobile_number = data["mob_number"]
        Validator.mandatory(name=name,email=email,mobile_number=mobile_number)
        print("successful til here")
        return {'message': 'Resource created successfully'}

