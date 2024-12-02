from marshmallow import Schema, fields, validate, ValidationError

# User schema for validating user-related data
class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    date_of_birth = fields.Date(required=True)

# Echo schema for validating echo data
class EchoSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(min=1))
    expires_at = fields.DateTime(required=True)
    # Add other fields as needed
    user_id = fields.Integer(required=True)
