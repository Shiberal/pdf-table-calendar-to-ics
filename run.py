import subprocess

def run_script(script_name):
    try:
        print(f"Running {script_name}")
        subprocess.run(["python3.11", script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    scripts = ["extract.py", "prune.py", "ical.py"]

    for script in scripts:
        run_script(script)

    print("All scripts have completed.")
