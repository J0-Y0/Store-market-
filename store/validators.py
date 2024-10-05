from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 100
    if file.size * 1024 > max_size_kb:
        raise ValidationError(f"file size should be less than {max_size_kb} KB")
