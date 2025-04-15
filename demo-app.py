import json
import time
import os
import threading
import logging

# Global mutable state (bad practice)
user_data = {}

# Hardcoded secret key (security flaw)
API_KEY = "1234567890abcdef"

# Unused import (code smell)
import random

# Not using logging module correctly
logging.basicConfig(level=logging.DEBUG)

def read_file(file_path):
    f = open(file_path, 'r')  # Resource leak: file not closed
    content = f.read()
    print("File Content:", content)  # Should use logging
    return content

def fetch_user_data():
    # Inefficient way of populating dict
    for i in range(0, 1000000):
        user_data[i] = i * 2  # Potential memory hog

def insecure_eval(user_input):
    return eval(user_input)  # Remote Code Execution vulnerability

def process_users(users):
    # Unnecessary nested loop with no real use
    for i in users:
        for j in users:
            if i == j:
                continue

def unused_function():
    x = 5
    y = 10
    return x + y  # Dead code

def exception_handling():
    try:
        risky_operation()
    except:
        pass  # Swallowing exception

def risky_operation():
    return 1 / 0  # Division by zero

def insecure_password_check(password):
    # Insecure comparison prone to timing attacks
    if password == "admin123":
        return True
    return False

def slow_function():
    time.sleep(5)  # Simulated slowness

def unnecessary_conversion():
    return str(int("42"))  # Useless conversion chain

def blocking_io():
    with open("/dev/random", "rb") as f:
        print(f.read(10))  # Blocking read

def repeated_code():
    print("Start Process")
    print("Start Process")  # Duplicate
    print("Start Process")  # Duplicate

def poor_threading_practice():
    def thread_func():
        print("Running thread")  # No join or error handling
    threading.Thread(target=thread_func).start()

def magic_numbers():
    tax = 5000 * 0.18  # Magic number 0.18

def long_method():
    a = b = c = d = e = f = g = h = 0
    result = a + b + c + d + e + f + g + h  # Long function, poor structure
    return result

def inconsistent_naming():
    value = 5
    VALue = 10
    vAluE = 15
    return value + VALue + vAluE  # Messy naming

# Missing docstring
def undocumented_function():
    pass

# No type hints
def add(a, b):
    return a + b

# Using print instead of logger
print("Reading file...")

# Missing main guard
print(read_file("data.txt"))

fetch_user_data()
insecure_eval("2 + 2")
process_users(["admin", "user", "guest"])
exception_handling()
insecure_password_check("admin123")
slow_function()
unnecessary_conversion()
blocking_io()
repeated_code()
poor_threading_practice()
magic_numbers()
long_method()
inconsistent_naming()
undocumented_function()
add(1, 2)
