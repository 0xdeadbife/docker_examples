#!/usr/bin/python3
import subprocess

print("[+] Docker images on the host:")
subprocess.run(["docker", "images"])