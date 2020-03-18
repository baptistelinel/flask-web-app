install_requirements:
	pip install -r requirements.txt

start_app:
	docker-compose up

destroy_app:
	make docker_rm
	make docker_rmi

connect_to_database:
	docker exec -it database psql products user

docker_rmi:
	docker rmi web_app_web
	docker volume rm `docker volume list -q`

docker_rm:
	docker stop web
	docker rm web
	docker stop database
	docker rm database