import hashlib

def hash_pii(pii_data, salt="G-SIFI-SALT-2035"):
    """
    Mandatory Salted SHA-256 hashing for all PII/MNPI identifiers in audit logs.
    Satisfies GDPR Article 25 and institutional security directives.
    """
    if not pii_data:
        return None

    salted_input = f"{pii_data}{salt}".encode('utf-8')
    return hashlib.sha256(salted_input).hexdigest()

if __name__ == "__main__":
    print(f"Hashed Identifier: {hash_pii('user_12345')}")
