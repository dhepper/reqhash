import os.path


def parse_requirements(req_filename):
    basedir = os.path.dirname(os.path.abspath(req_filename))
    with open(req_filename) as req_file:
        normalized = normalize_reqs(req_file)
    requirements = []
    for line in normalized:
        if line.startswith('-r') or line.startswith('--requirement'):
            if line.startswith('-r'):
                rel_ref_path = line[2:].strip()
            else:
                rel_ref_path = line[len('--requirement'):].strip().strip('=')
            abs_ref_path = os.path.join(basedir, rel_ref_path)
            requirements.extend(parse_requirements(abs_ref_path))
        else:
            requirements.append(line)
    return requirements


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
        uncommented = stripped.split(' #')[0].strip()
        normalized.append(uncommented)
    return normalized
