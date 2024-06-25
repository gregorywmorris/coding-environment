import toml

def extract_dependencies(tomlfile_path, output_path):
    # Load the TOML file
    with open(tomlfile_path, 'r') as f:
        toml_data = toml.load(f)

    # Extract dependencies from the `tool.pdm.dependencies` section
    dependencies = toml_data.get('tool', {}).get('pdm', {}).get('dependencies', [])

    with open(output_path, 'w') as f:
        for dep in dependencies:
            # If the dependency is a dictionary, it might have additional information
            if isinstance(dep, dict):
                for name, version in dep.items():
                    f.write(f"{name}=={version}\n")
            else:
                # Directly write the dependency if it's a string
                f.write(f"{dep}\n")

# Specify the path to your pyproject.toml file and the output requirements.txt file
tomlfile_path = 'pyproject.toml'
output_path = 'requirements.txt'

extract_dependencies(tomlfile_path, output_path)
