def write_file(data: str):
    with open('README.md', 'w') as f:
        f.write(data.lstrip())
