from collections import deque
class task(object):
    def __init__(self, taskDesc, hasPriority = False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority
    def __str__(self):
        return "Task {0}, Priority {1}".format(self.taskDesc, self.hasPriority)

taskQ = deque()
def addTask(task):
    if task.hasPriority:
        taskQ.appendleft(task)
    else:
        taskQ.append(task)
def DoTask():
    return taskQ.popleft()
def printTask():
    for i in taskQ:
        print(i.taskDesc)
def main():
    addTask(task("Make list"))
    addTask(task("Make breakfast"))
    addTask(task("Pay bills", True))
    printTask()
    print(DoTask())
    return

if __name__ == "__main__":
    main()