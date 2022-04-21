from cerberus import Validator


def validate_cus_add(data):
    schema = {'name': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z\s.]*$'}}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


def validate_acc_add(data):
    schema = {'customer_id': {'type': 'integer', 'empty': False},
              'acc_no': {'type': 'string', 'empty': False, 'regex': '[0-9]{10}'},
              'balance': {'type': 'integer', 'empty': False},
              'link_code': {'type': 'integer', 'empty': False}, }
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


# def validate_ca_add(data):
#     schema = {'customer_id': {'type': 'integer', 'empty': False},
#               'acc_no': {'type': 'string', 'empty': False, 'regex': '[0-9]{10}'},
#               'balance': {'type': 'integer', 'empty': False},
#               'link_code': {'type': 'integer', 'empty': False}, }
#     v = Validator(schema)
#     if v.validate(data, schema):
#         return True
#     else:
#         return v.errors
