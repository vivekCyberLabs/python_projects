import socket
import threading
import queue

ip = socket.gethostbyname("scanme.nmap.org")
print(ip)
queue = queue.Queue()
for p in range(1,1001):
    queue.put(p)
def scan():
     while not queue.empty():
        port = queue.get()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex((ip, port))
                s.settimeout(0.5)
                if result == 0:
                    print(f"Port {port} is open")
        except:
            pass
        queue.task_done()

for t in range(30):
    scan_thread = threading.Thread(target=scan,daemon=True)
    scan_thread.start()

queue.join()
print("Finished")








