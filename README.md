# In-Memory Key-Value Database

A command-line, in-memory key-value store built in Python, with persistence and TTL (key expiration) support. Built for the EHAX project.

## Features

- **Core commands:** `SET`, `GET`, `DEL`, `EXISTS`
- **Persistence:** `SAVE <filename>` / `LOAD <filename>` — dumps/restores the in-memory store to/from a JSON file
- **Key expiration (TTL):** `SETEX <key> <seconds> <value>` — automatically expires keys after a set duration (lazy expiration, checked on access)
- **Bulk delete:** `DEL *` clears the entire store
- **Built-in help:** `MAN` lists all available commands
- **Clean exit:** `QUIT`

## Requirements

- Python 3.x (standard library only — no third-party packages required)

## Usage

```bash
python memdb.py
```

Example session:
```
memdb -> SET name "Akshat Budhori"
Value set
memdb -> GET name
Akshat Budhori
memdb -> SETEX session 30 active
OK
memdb -> SAVE data.json
Saved to database
memdb -> EXISTS name
Exists
memdb -> DEL name
Value deleted
memdb -> QUIT
Exit
```

## Commands reference

| Command | Description |
|---|---|
| `SET <key> <value>` | Store a key-value pair |
| `GET <key>` | Retrieve the value for a key |
| `DEL <key>` | Delete a key (or `DEL *` to clear everything) |
| `EXISTS <key>` | Check whether a key exists |
| `SETEX <key> <seconds> <value>` | Store a key that automatically expires after the given number of seconds |
| `SAVE <filename>` | Persist the current store to a file |
| `LOAD <filename>` | Restore the store from a previously saved file |
| `MAN` | Show the command list |
| `QUIT` | Exit the program |

## Design notes

- Values are stored internally as `{"value": ..., "expiry": ...}` to support TTL alongside plain key-value pairs.
- Expiration is **lazy**: a key's expiry is checked at the moment it's accessed (`GET`/`EXISTS`), not via a background process — this keeps the implementation simple with no extra threads.
- Persistence uses Python's built-in `json` module; no external database or caching library is used, per project constraints.

## Project structure

```
memdb.py        # entry point — REPL loop
commands.py     # command parsing and dispatch logic
database.py     # SAVE/LOAD persistence (JSON-based)
help.py         # MAN command output
```

## Constraints followed

- No database or caching libraries (no SQLite, Redis-py, etc.)
- Only standard library built-ins used throughout

## Known limitations

- No literal quote characters in values — `shlex` uses them as delimiters and strips them
- All values are stored as strings, no numeric/boolean typing
- Flat key-value namespace only, no multi-record or nested structures
- Not safe for concurrent access (single in-memory dict, no locking)
- SAVE is not atomic — an interrupted write could corrupt the file
