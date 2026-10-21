from django.core.exceptions import ValidationError


def _validate_key_value_type(key, value, _type):
    match _type:
        case "boolean" if not isinstance(value, bool):
            raise ValidationError(f"The key '{key}' must be a boolean.")
        case "integer" if not isinstance(value, int):
            raise ValidationError(f"The key '{key}' must be an integer.")
        case "array" if not isinstance(value, list):
            raise ValidationError(f"The key '{key}' must be a list.")
        case "object" if not isinstance(value, dict):
            raise ValidationError(f"The key '{key}' must be an object.")
        case "string" if not isinstance(value, str):
            raise ValidationError(f"The key '{key}' must be a string.")
