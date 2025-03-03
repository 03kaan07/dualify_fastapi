import subprocess
import json

def run_noten_script(username: str, password: str):
    # Define your command
    command = ["bash", "app/dualis/NOTEN.sh", "-u", username, "-p", password]

    # Run the command and capture both stdout and stderr
    result = subprocess.run(command, capture_output=True, text=True)

    # Get the output from stdout and stderr
    output = result.stdout.strip()
    error_output = result.stderr.strip()

    # Print raw output for debugging
    print("📥 Raw Output:", output)
    print("⚠️ Error Output:", error_output)

    # Try to parse the output as JSON
    try:
        json_data = json.loads(output)
        return json_data
    except json.JSONDecodeError:
        print("❌ Error: The output is not valid JSON.")
        return None