#!/usr/bin/python3

import subprocess
import os
import sys
import time

# Centralized environment configuration
BUILD_ENV = {
    **os.environ,
    "NOJESSIE": "1",
    "NOSTRETCH": "1",
    "NOBUSTER": "1",
    "NOBULLSEYE": "1",
    "BLDENV": "bookworm",
    "CROSS_BLDENV": "1",
    "DOCKER_BUILDKIT": "0",
    "SONIC_BUILD_JOBS": "4",
    "DOCKER_DATA_ROOT_FOR_MULTIARCH": "/var/lib/march/docker",
    "BUILD_SONIC_BMC": "y",
    "PLATFORM": "broadcom",
    "PLATFORM_ARCH": "arm64"
}

def run_step(description, command):
    """Executes a command and automatically feeds 'sonic' as input."""
    print(f"\n--- [ {description} ] ---")
    start_time = time.time()

    # Prefixing the command with 'yes sonic |' to auto-fill prompts
    interactive_command = f"yes sonic | {command}"

    try:
        subprocess.run(
            interactive_command,
            shell=True,
            env=BUILD_ENV,
            check=True,
            executable='/usr/bin/bash'
        )

        duration = time.time() - start_time
        print(f"DONE: {description} ({duration:.2f}s)")

    except subprocess.CalledProcessError as e:
        print(f"\nSTOPPED: {description} failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def main():
    total_start = time.time()

    # Step 1: Load Overlay Module
    run_step("Load Overlay Module", "sudo modprobe overlay")

    # Step 2: Init
    run_step("Init", "make init")

    # Step 3: Configure
    run_step("Configure", "make configure")

    # Step 4: List Targets
    run_step("List Targets", "make list | tee targets_ast2720_arm64")

    # Step 5: Build Image
    run_step("Build Image", "make target/sonic-aboot-broadcom.swi | tee buildlog.log")

    total_duration = (time.time() - total_start) / 60
    print(f"\n{'='*40}")
    print(f"BUILD FINISHED in {total_duration:.2f} minutes")
    print(f"{'='*40}")

if __name__ == "__main__":
    main()
