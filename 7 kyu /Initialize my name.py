def initialize_names(name):
    parts = name.split()
    if len(parts) <= 2:
        return name
    for i in range(1, len(parts) - 1):
        parts[i] = parts[i][0] + '.'
    return ' '.join(parts)
