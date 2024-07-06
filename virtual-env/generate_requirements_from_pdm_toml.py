import toml

def extract_dependencies(tomlfile_path, output_path):
    try:
        # Load the TOML file
        with open(tomlfile_path, 'r') as f:
            toml_data = toml.load(f)
    except Exception as e:
        print(f"Error loading TOML file: {e}")
        return

    # Extract dependencies from the `project.dependencies` section
    dependencies = toml_data.get('project', {}).get('dependencies', [])

    if not dependencies:
        print("No dependencies found in the specified section.")
        return

    with open(output_path, 'w') as f:
        for dep in dependencies:
            f.write(f"{dep}\n")

    print(f"Dependencies have been written to {output_path}")

# Specify the path to your pyproject.toml file and the output requirements.txt file
tomlfile_path = 'pyproject.toml'
output_path = 'requirements.txt'

extract_dependencies(tomlfile_path, output_path)
