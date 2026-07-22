# Thread with arguments and Daemon 

import threading 
import time

class AdvancedWorker(threading.Thread):
    def __init__(self, name ,delay, daemon = False):

        # Initialize the base thread class
        super().__init__()

        self.name = f"Worker-{name}"
        self.delay = delay
        # Flag indication if this should behave as a daemon thread
        self.daemon = daemon

        # Internal Flag used to stop the loop in run()
        self._stop_flag = False

    def run(self):
        print(f"Thread {self.name}: Started")

        while not self._stop_flag:
            print(f"Thread {self.name}: Working")
            time.sleep(self.delay)

        print(f"Thread {self.name}: Stopped")

    def stop(self):
        print(f"Thread {self.name}: Stop Requested")
        self._stop_flag = True


def demonstrate_daemon():
    print("Creating Daemon Thread")
    daemon_thread = AdvancedWorker("Daemon" , 1,daemon = True)

    daemon_thread.start()


    print("Creating non-Daemon Thread")
    daemon_thread = AdvancedWorker("Worker" , 1,daemon = True)

    daemon_thread.start()

demonstrate_daemon()

def proper_thread_cleanup():
    workers = []

    for i in range(3):
        worker = AdvancedWorker(f"W{i}",1)
        worker.daemon = True
        worker.start()
        workers.append(worker)

    print("Main : Letthe workers run for 5 Seconds")
    time.sleep(5)

    for worker in workers:
        worker.stop()

    for worker in workers:
        worker.join(timeout = 2)

    print("Main: All threads cleaned up")

proper_thread_cleanup()