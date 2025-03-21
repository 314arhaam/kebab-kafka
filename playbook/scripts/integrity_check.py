import sys, subprocess

if __name__ == '__main__':
    control_file = sys.argv[1]
    download_file = sys.argv[2]
    with open(control_file, 'r') as cfile:
        sha512control = cfile.read()
    sha512control = ''.join(sha512control.replace('\n', '').split()[1:]).lower()
    sha512download = subprocess.run(f"sha512sum {download_file}", shell=True, capture_output=True)
    sha512download = sha512download.stdout.decode().split()[0]
    print(sha512download, sha512control)
