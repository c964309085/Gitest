import _thread

def child(tid):
    print("Hello from thread",tid)
def parent():
    