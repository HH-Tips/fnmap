#!/usr/bin/env python3
import argparse
import os
import subprocess
import datetime
import sys

def main():
    parser = argparse.ArgumentParser(
        description="fnmap: A fast Python wrapper for nmap to streamline scanning and organization.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  fnmap -F 192.168.1.1       # Full scan (all ports)
  fnmap -c 192.168.1.1       # Common port scan
  fnmap -f 192.168.1.1       # Fast scan (top 100 ports)
        """
    )
    
    parser.add_argument("target", help="Target IP address, hostname, or range (e.g., 192.168.1.1/24)")
    
    # Scan Mode Group
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-F", "--full", action="store_true", help="Full scan (scans all 65535 ports: -p-)")
    group.add_argument("-c", "--common", action="store_true", help="Common port scan (default nmap ports)")
    group.add_argument("-f", "--fast", action="store_true", help="Fast scan (top 100 ports: -F)")
    
    # Options
    parser.add_argument("-r", "--rate", type=int, default=1000, help="Packet rate (default: 1000)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--sudo", action="store_true", help="Run nmap with sudo (required for some scan types)")

    args, extra_nmap_args = parser.parse_known_args()

    # Define mode and specific nmap flags (Default to common if none selected)
    if args.full:
        mode = "full"
        nmap_flags = ["-p-"]
    elif args.fast:
        mode = "fast"
        nmap_flags = ["-F"]
    else:
        # Default mode is 'common'
        mode = "common"
        nmap_flags = []


    # Set up output directory: $(pwd)/nmap/
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "nmap")
    
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"[*] Created directory: {output_dir}")
    except Exception as e:
        print(f"[-] Error creating directory: {e}")
        sys.exit(1)

    # Output filename: nmap/<modalità>
    output_base = os.path.join(output_dir, mode)


    # Construct the nmap command
    cmd = []
    if args.sudo:
        cmd.append("sudo")
    
    cmd.extend(["nmap", "--min-rate", str(args.rate), "-sV", "-sC"])
    
    # Add specific mode flags
    cmd.extend(nmap_flags)
    
    # Add auto-save flags (Output in all formats: .nmap, .xml, .gnmap)
    cmd.extend(["-oA", output_base])
    
    if args.verbose:
        cmd.append("-v")
    
    # Add extra nmap arguments provided by the user
    if extra_nmap_args:
        cmd.extend(extra_nmap_args)
    
    # Add the target
    cmd.append(args.target)


    # Execution
    print(f"\n{'='*60}")
    print(f"  FNMAP - {mode.upper()} SCAN")
    print(f"{'='*60}")
    print(f"[*] Target      : {args.target}")
    print(f"[*] Rate        : {args.rate}")
    print(f"[*] Output Base : {output_base}")
    print(f"[*] Command     : {' '.join(cmd)}")
    print(f"{'='*60}\n")

    try:
        # We use subprocess.run with check=True to ensure we catch errors.
        # Output is streamed to stdout naturally.
        subprocess.run(cmd, check=True)
        print(f"\n[+] Scan completed successfully.")
        print(f"[+] Results saved in: {output_dir}/")
    except subprocess.CalledProcessError as e:
        print(f"\n[-] Error: nmap exited with non-zero status ({e.returncode}).")
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n[-] Error: 'nmap' command not found. Please ensure nmap is installed.")
    except Exception as e:
        print(f"\n[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
