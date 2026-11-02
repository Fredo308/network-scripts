#!/usr/bin/env python3
"""
Network Audit & Interface Diagnostic Tool
Automates network interface status checks, routing validation, and environment diagnostics.
"""

import subprocess
import sys

def check_interfaces():
    print("[+] Auditing Network Interfaces...")
    try:
        result = subprocess.run(["ip", "link", "show"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"[-] Error querying interfaces: {e}")

def check_routing_table():
    print("[+] Auditing Routing Table...")
    try:
        result = subprocess.run(["ip", "route", "show"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"[-] Error querying routes: {e}")

if __name__ == "__main__":
    print("--- Starting Network Health Diagnostics ---")
    check_interfaces()
    check_routing_table()
    print("--- Audit Completed ---")
