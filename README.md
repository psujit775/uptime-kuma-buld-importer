# uptime-kuma-buld-importer
Simple script to bulk import domains in uptime kuma.

Create a hosts.txt file.
Sample:
```
somedomain.com
https://anotherhost.org
example.org
subdomain.example.org
```


command: `python3 import.py`

This will generate a backup.json file which you can import in the uptime kuma ui.
