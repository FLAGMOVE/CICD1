#!/bin/bash
set -e

SERVER_USER="super"
SERVER_IP="192.168.56.107"
PROJECT_PATH="/home/super/CICD1"

rsync -avz --exclude '.git' . "$SERVER_USER@$SERVER_IP:$PROJECT_PATH"

ssh "$SERVER_USER@$SERVER_IP" << EOF
cd $PROJECT_PATH
sudo systemctl restart mortgage.service
EOF
