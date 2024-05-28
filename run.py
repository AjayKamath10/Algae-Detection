import subprocess
import os


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True)
    stdout = result.stdout.decode('utf-8') if result.stdout else None
    stderr = result.stderr.decode('utf-8') if result.stderr else None
    return stdout, stderr


def main():
    print("Choose an option:")
    print("1. Predict Point")
    print("2. Predict from CSV")

    choice = input("Enter the number of your choice: ")
    # run_command("conda activate cyfienv")
    if choice == '1':
        latitude = input("Enter latitude: ")
        longitude = input("Enter longitude: ")
        date = input("Enter date (YYYY-MM-DD): ")

        command = f"cyfi predict-point --lat {latitude} --lon {longitude} --date {date}"
        print(f"Running prediction")
        stdout, stderr = run_command(command)
        if stderr:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")

    elif choice == '2':
        csv_path = input("Enter the CSV path: ")
        directory_name = input("Enter the directory name for metadata: ")

        command = f"cyfi predict {csv_path} --keep-metadata -d {directory_name}"
        print("Prediction is running. Please wait")
        stdout, stderr = run_command(command)
        if stderr:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")

        visualization_command = f"cyfi visualize {directory_name}/"
        print("Preparing Visualization... Please wait")
        print("Visualization will run on local URL:  http://127.0.0.1:7860")
        stdout, stderr = run_command(visualization_command)

        if stderr:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == '__main__':
    main()
