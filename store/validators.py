from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 100
    max_size_bytes = max_size_kb * 1024  # Convert KB to bytes
    if file.size > max_size_bytes:
        raise ValidationError(f"File size should be less than {max_size_kb} KB")
