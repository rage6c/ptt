from flask import request


class RequestTypeConvertor:
    @staticmethod
    def convert_to(class_):
        def wrap(f):
            def decorator():
                obj = class_.from_dict(request.json)
                return f(obj)
            return decorator
        return wrap
