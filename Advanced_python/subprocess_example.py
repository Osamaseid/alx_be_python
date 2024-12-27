import subprocess

# Execute a shell command
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
print(result.stdout)  # Outputs: Hello, World!