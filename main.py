import subprocess
import sys
import os

def run(cmd: str) -> subprocess.Popen:
    # print(cmd.split())
    return subprocess.Popen(
        cmd.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

def main():
    if len(sys.argv) == 1:
        print("Please specify a package to search", file=sys.stderr)
        sys.exit(1)

    target_package = str(sys.argv[1])

    found: bool = False

    processes = [
        ("dnf", run("dnf list --installed")),
        ("flatpak", run("flatpak list")),
    ]

    for packet_mgr, process in processes:
        output = process.communicate()[0]
        if output == b"":
            print(f"{packet_mgr} did not output anything")
            continue

        if target_package.encode().lower() not in output.lower():
            # print(f"{packet_mgr} did not output anything")
            continue

        print(f"Package {target_package} was installed using {packet_mgr}")
        found = True

    if found:
        return

    for path in os.environ.get("PATH").split(":"):
        if not os.path.exists(path):
            # print(f"[WARN] '{path}' does not exist")
            continue
        for file in os.listdir(path):
            if target_package.lower() in file.lower():
                print(f"Found {file} in {path}")
                found = True

    if not found:

        print(f"Could not find the packet mgr {target_package} was installed with")


if __name__ == "__main__":
    main()
