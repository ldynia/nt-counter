#!/bin/ash
# Docker startup script

echo "Ssh deamon started in foreground"
/usr/sbin/sshd -D

exec "$@"
