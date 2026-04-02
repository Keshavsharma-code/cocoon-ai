import hashlib

def generate_larva_id(name: str) -> str:
    """Generates a unique, authenticated ID for a larva."""
    return hashlib.sha256(name.encode()).hexdigest()[:12]
