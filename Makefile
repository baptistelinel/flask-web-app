install_requirements:
	pip install -r requirements.txt

start_app:
	docker-compose up

destroy_app:
	make docker_rm
	make docker_rmi

docker_rmi:
	docker rmi web_app_web
	docker rmi web_app_database

docker_rm:
	docker stop web
	docker rm web
	docker stop database
	docker rm database