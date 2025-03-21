import sys, subprocess

if __name__ == '__main__':
    # control file as the first arg
    control_file = sys.argv[1]
    # downloaded file for sum as the second arg
    download_file = sys.argv[2]
    # open & read control file
    with open(control_file, 'r') as cfile:
        sha512control = cfile.read()
    # clear all text other than code and make it lower case
    sha512control = ''.join(sha512control.replace('\n', '').split()[1:]).lower()
    # run sha512sum and capture output
    sha512download = subprocess.run(f"sha512sum {download_file}", shell=True, capture_output=True)
    # extract main string
    sha512download = sha512download.stdout.decode().split()[0]
    print(sha512download, sha512control)
    # if not equal raise value rror
    if sha512download != sha512control:
        raise ValueError("SHA512SUM of the downloaded files is not equal to the validated keys")
