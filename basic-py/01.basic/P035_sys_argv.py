import sys



DEBUG = True

def lognow()
    print(DEBUG)

if __name__ == "__main__":
    options = sys.argv
    print(">>>>> options: ", options)
    if len(options) < 2:
        print("Requirements Unsatisfied, Abort")
        sys.exit(1)
    print(">>>>> options: ", options)
    with open(LOGFILE, 'w') as wf:
        # status = main(wf)
        lognow(wf, "Checking debugging variables")
    print("Task Completed")
    