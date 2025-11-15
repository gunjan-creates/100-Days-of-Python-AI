"""Executes a subprocess and captures its output."""
import subprocess

if __name__ == "__main__":
    result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True, check=True)
    print("Return code:", result.returncode)
    print("Stdout:", result.stdout.strip())
