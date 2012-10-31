def parse_requirements(req_file):
    requirements = normalize_reqs(req_file)
    pass

def normalize_reqs(requirements):
    """
    Normalize requirement file.

    Strips comments and whitespace
    """
    normalized = []
    for line in requirements:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        normalized.append(stripped)
