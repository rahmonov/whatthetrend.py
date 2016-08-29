import json


class JSONResponse:
    def __new__(cls, ok=False, data=None, message=None, status=None, *args, **kwargs):
        if message:
            return {'ok': ok, 'message': message, 'status': status}

        return {'ok': ok, 'data': json.dumps(data)}
