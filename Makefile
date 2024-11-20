docker-spin-up:
	docker compose up --build -d

up: docker-spin-up 

down:
	docker compose down 

clean:
	find CreditSpring -type d -name '__pycache__' -exec rm -rf {} +
	find CreditSpring -mindepth 1 -maxdepth 1 \
		! -name 'data_loaders' \
		! -name 'data_exporters' \
		! -name 'transformers' \
		! -name 'pipelines' \
		-exec rm -rf {} +
	rm -rf mage_data  

restart: down clean up

teardown: down clean