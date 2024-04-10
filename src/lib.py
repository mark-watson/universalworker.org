import subprocess

def applescript_to_text(script_file_path):
    with open(script_file_path, "r") as f:
        script = f.read()
    args = ["osascript", "-e", script]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    stdout, stderr = result.stdout, result.stderr
    return stdout, stderr
