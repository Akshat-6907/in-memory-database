from database import save, load
from help import manual
import time

def command(parts, store):
    cmd = parts[0].upper()

    if cmd == "SET" and len(parts) == 3:
        store[parts[1]] = {"value": parts[2], "expiry": None}
        print("Value set")

    elif cmd == "SETEX" and len(parts)==4:
        key , seconds , value = parts[1], parts[2], parts[3]
        try :
            seconds = float(seconds)
        except ValueError:
            print("ERROR : seconds must be a number")
        else :
            store[key] = {"value" : value , "expiry" : time.time() + seconds}
            print("Value set")

    elif cmd == "GET" and len(parts) == 2:
        key = parts[1]
        if key in store :
            entry = store[key]
            if entry["expiry"] is not None and time.time() > entry["expiry"]:
                del store[key]
                print("ERROR : key not found")
            else :
                print(entry["value"])
        else :
            print("ERROR : key not found")

    elif cmd == "DEL" and len(parts) == 2:
        if parts[1] in store and parts[1] != "*":
            del store[parts[1]]
            print("Value deleted")
        elif parts[1]=="*":
            store.clear()
            print("Cleared")
        else:
            print("ERROR: key not found")

    elif cmd == "EXISTS" and len(parts) == 2:
        key = parts[1]
        if key in store :
            entry = store[key]
            if entry["expiry"] is not None and time.time()>entry["expiry"] :
                del store[key]
                print("Does not exist")
            else :
                print("Exists")
        else : 
            print("Does not exist")

    elif cmd == "SAVE" and len(parts) == 2:
        save(store, parts[1])
        print("Saved to database")

    elif cmd == "LOAD" and len(parts) == 2:
        load(store, parts[1])

    elif cmd == "MAN" and len(parts)==1:
        manual()

    else:
        print("ERROR: unknown command or wrong number of arguments")
