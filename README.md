# CLIPBOARD SCAN
Script sencillo para almacenar todo lo que copiamos al portapapeles el portapapeles


Configurar en crontab

```* * * * * /home/ricardo/Workspace/Python/clipboard-scan/read-clipboard.sh >> /home/ricardo/Workspace/Python/clipboard-scan/cron.log 2>&1```

ó

```* * * * * /home/ricardo/Workspace/Python/clipboard-scan/read-clipboard.sh```