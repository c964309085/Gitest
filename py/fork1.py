"forks child process until you type 'q'"
import  os
def child():
    print('Hello from child',os.getpid())
    os._exit(0) # else goes back to parent loop
##父进程和子进程内返回。子进程永远返回0，而父进程返回子进程的 PID。我们可以通过判断返回值是不是 0 来判断当前是在父进程还是子进程中执行
def parent():
    while True:
        newpid=os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent',os.getpid(),newpid)
        if input() == 'q':break
parent()
