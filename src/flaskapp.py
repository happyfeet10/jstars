from flask import Flask
from multiprocessing import Process,Queue
app = Flask(__name__)
world = "None"

@app.route("/")
def getWorld():
    global world
    while not pqueue.empty():
        world = pqueue.get()
    return world

def exportServer(queue):
    for i in range(0,10):
        queue.put(f"QUEUE {i}")

if __name__ == "__main__":
    pqueue = Queue()
    exportprocess = Process(target=exportServer, args=((pqueue),))
    exportprocess.start()
    app.run()
    exportprocess.join()
