from cerberus import Validator


def validate_cus_add(data):
    schema = {'name': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z\s.]*$'},
              'phone': {'type': 'string', 'empty': False, 'maxlength': 10, 'regex': '^[0-9]{10}'}}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


def validate_prd_add(data):
    schema = {'name': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z0-9\s.]*$'},
              'category': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z0-9\s.]*$'},
              'brand': {'type': 'string', 'empty': False, 'maxlength': 50, 'regex': '^(?![\s.]+$)[a-zA-Z0-9\s.]*$'},
              'price': {'type': 'integer', 'empty': False, }}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


def validate_bill_add(data):
    schema = {
        'customer_id': {'type': 'string', 'empty': False, 'maxlength': 20, 'regex': '[a-zA-Z0-9]{3}-?[a-zA-Z0-9]{4}'}}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors


def validate_bill_detail_add(data):
    schema = {'product_id': {'type': 'integer', 'empty': False, },
              'quantity': {'type': 'integer', 'empty': False, }}
    v = Validator(schema)
    if v.validate(data, schema):
        return True
    else:
        return v.errors

