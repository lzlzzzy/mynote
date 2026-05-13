#!/usr/bin/env python3
"""
setup_password.py — Generate password hash for the Notes Notebook app.

Usage:
    python setup_password.py
    python setup_password.py "your-password-here"

This script computes a SHA-256 hash of your password and outputs a config
snippet to paste into index.html's window.__CONFIG__ block.

After setting the password, update the PASSWORD_HASH value in index.html
and re-deploy to GitHub Pages.
"""

import hashlib
import sys


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        import getpass
        password = getpass.getpass("Enter password: ")
        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Error: Passwords do not match.")
            sys.exit(1)

    if not password:
        print("Error: Password cannot be empty.")
        sys.exit(1)

    hashed = hash_password(password)

    print("\n" + "=" * 60)
    print("  Password hash generated successfully!")
    print("=" * 60)
    print()
    print("Update your index.html with this config:\n")
    print("  window.__CONFIG__ = {")
    print(f'    PASSWORD_HASH: "{hashed}",')
    print('    GITHUB_OWNER: "your-username",')
    print('    GITHUB_REPO: "your-repo-name",')
    print('    GITHUB_BRANCH: "main",')
    print("  };")
    print()
    print("=" * 60)
    print("  How to create a GitHub fine-grained PAT:")
    print("  1. Go to GitHub Settings → Developer settings → Personal access tokens")
    print("  2. Create a Fine-grained token with access to your notes repo")
    print("  3. Repository permissions: Contents (Read and write)")
    print("  4. You'll enter this token in the app's config dialog on first use")
    print("=" * 60)


if __name__ == "__main__":
    main()
