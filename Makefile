install_requirements:
	pip install -r requirements.txt

start_app:
	docker-compose up

destroy_app:
	make docker_rm
	make docker_rmi
	docker volume rm `docker volume list -q`

run_migrations:
	docker exec -it web alembic --config migrations/alembic.ini upgrade head

connect_to_database:
	docker exec -it database psql supermarket user

docker_rmi:
	docker rmi web-app_web
	docker rmi web-app_database

docker_rm:
	docker stop web
	docker rm web
	docker stop database
	docker rm database