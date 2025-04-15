import json
import time
import os

# Global variables (bad practice)
user_data = {}

# Hardcoded secrets (security issue)
API_KEY = "1234567890abcdef"

def read_file(file_path):
    f = open(file_path, 'r')  # File not closed (resource leak)
    return f.read()

def fetch_user_data():
    # Inefficient loop
    for i in range(0, 1000000):
        user_data[i] = i * 2

def insecure_eval(user_input):
    return eval(user_input)  # Dangerous: Potential RCE

def process_users(users):
    # Nested loop with O(n^2) complexity
    for i in users:
        for j in users:
            if i == j:
                continue

def unused_function():
    x = 5
    y = 10
    return x + y  # Never called (dead code)

def exception_handling():
    try:
        risky_operation()
    except:
        pass  # Swallowing exception (bad practice)

def risky_operation():
    return 1 / 0  # Division by zero error

def insecure_password_check(password):
    # Insecure string comparison (timing attack possible)
    if password == "admin123":
        return True
    return False

def slow_function():
    time.sleep(5)  # Unnecessary delay

# Missing if __name__ == '__main__' guard
print("Reading file...")
print(read_file("data.txt"))

fetch_user_data()
