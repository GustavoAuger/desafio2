from marshmallow import Schema, fields, validate

# campos

class TaskModel:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status


#para validaciones de entrada en la api
class TaskSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=False, validate=validate.Length(max=255))
    status = fields.String(
        validate=validate.OneOf(["pendiente", "completado"]),
        missing="pendiente"  # Valor por defecto
    )
