install_requirements:
	pip install -r requirements.txt

start_app:
	docker build -t blinel/web_app .
	docker-compose up

docker_rmi:
	docker rmi blinel/web_app:latest
	docker rmi python
	docker rmi postgres

docker_rm:
	docker stop web_app
	docker rm web_app
	docker stop postgres
	docker rm postgres