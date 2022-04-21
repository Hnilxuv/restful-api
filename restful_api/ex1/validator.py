from cerberus import Validator


def validate_add(data):
    schema = {'name': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z\s.]*$'},
              'acc_no': {'type': 'string', 'empty': False, 'regex': r'[0-9]{9}'},
              'balance': {'type': 'integer', 'empty': False}}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


def validate_amount(data):
    schema = {'amount': {'type': 'integer', 'empty': False}}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors
