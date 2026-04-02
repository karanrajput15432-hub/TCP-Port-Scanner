import socket
import threading

# Target input
target = input("Enter the domain name or IP: ")

# Try converting domain → IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target!")
    exit()

start_port = 20
end_port = 200

print(f"\nScanning target: ({target_ip}) from {start_port} to {end_port}...\n")

found_open = False   #  track open ports


#  Service detection
def get_service(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_ip, port))

        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()

        return banner if banner else "Unknown"

    except:
        return "No response"


#  Scan function
def scan(port):
    global found_open

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            found_open = True
            service = get_service(port)
            print(f"[OPEN] Port {port} --> {service}")

        s.close()

    except:
        pass


threads = []

#  Create threads
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

#  Wait for all threads
for t in threads:
    t.join()

#  Handle case when no ports are open
if not found_open:
    print("No open ports found.")

print("\nScanning completed.")