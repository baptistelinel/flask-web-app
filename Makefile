install_requirements:
	pip install -r requirements.txt

docker_build:
	docker build -t blinel/web_app_docker .

docker_run:
	docker run --name web_app_docker -d -p 8888:5000 blinel/web_app_docker

docker_exec:
	docker exec -it web_app_docker bash

docker_rmi:
	docker rmi blinel/web_app_docker:latest

docker_rm:
	docker stop web_app_docker
	docker rm web_app_docker