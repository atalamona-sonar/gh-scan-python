"""Synthetic demo code with deliberate issues for scan exploration."""
import hashlib
import subprocess

API_KEY = "sk_live_1234567890abcdef"  # hardcoded secret


def add(a, b):
    return a + b


def checksum(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()  # weak hash


def run(cmd: str) -> str:
    # command injection risk
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


def classify(n):
    if n > 0:
        return "pos"
    elif n < 0:
        return "neg"
    elif n == 0:
        return "zero"
    else:
        return "zero"  # unreachable, duplicated branch
