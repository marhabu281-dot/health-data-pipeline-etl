import hashlib

def hash_identifier(value: str) -> str:
    """Hashes a direct patient identifier using SHA-256 for privacy compliance."""
    if not value or str(value).strip() == '':
        return None
    return hashlib.sha256(str(value).encode('utf-8')).hexdigest()