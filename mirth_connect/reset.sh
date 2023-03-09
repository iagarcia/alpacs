sudo docker ps -aq | sudo xargs docker stop | sudo xargs docker rm
sudo docker system prune --all
sudo rm -rf appdata/*
sudo docker-compose up
