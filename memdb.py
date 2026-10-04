import shlex
from commands import command

def separator():
    print("-"*80)

def main():
    store = {}
    while True :
        try :
            print("{use MAN for help manual}")
            line = input("memdb -> ")
        except EOFError:
            break
        if not line.strip():
            continue
        try:
            parts = shlex.split(line)
            if parts[0].upper()=="QUIT":
                print("Execution finished")
                separator()
                break
        except ValueError as e:
            print(f"ERROR : {e}")
            separator()
            continue
        command(parts, store)
        separator()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecution Finished")
        separator()