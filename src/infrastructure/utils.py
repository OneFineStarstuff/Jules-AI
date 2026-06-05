import hashlib

def hash_pii(identifier, salt="SENTINEL_SALT_2026"):
    """
    Hashes PII using Salted SHA-256 as mandated by AGENTS.md.
    Ensures that audit logs never contain raw sensitive identifiers.
    """
    if not identifier:
        return None
    salted_input = f"{identifier}|{salt}"
    return hashlib.sha256(salted_input.encode()).hexdigest()

if __name__ == "__main__":
    print(f"Hashed ID: {hash_pii('SOCIAL_SECURITY_NUMBER')}")
