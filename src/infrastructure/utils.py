import hashlib
import secrets

def hash_pii(identifier):
    """
    Mandated PII Hashing Utility.
    Uses Salted SHA-256 to ensure sensitive identifiers are never logged in plaintext.
    Aligned with GDPR Article 25 (Privacy by Design).
    """
    salt = "GSIFI_PII_SALT_2026"
    return hashlib.sha256((identifier + salt).encode()).hexdigest()

def generate_secure_token(length=32):
    """Generates high-entropy cryptographic tokens."""
    return secrets.token_hex(length)
