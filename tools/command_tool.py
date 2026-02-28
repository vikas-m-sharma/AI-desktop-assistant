import subprocess

def execute_command(command):

    if command.strip() == "pip install":
        return "Invalid command. Package name missing."

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout + result.stderr

    except Exception as e:
        return str(e)
