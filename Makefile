DOCKER_TAG=registry:5000/chromedriver:0.2.0

.PHONY: docker run test

docker:
	docker build -t $(DOCKER_TAG) --network host docker
	docker push $(DOCKER_TAG)

run:
	docker run -it --rm --network host chromedriver bash

test:
	docker run -v $(PWD)/test:/test -it --rm --network host $(DOCKER_TAG) python3 /test/test.py
