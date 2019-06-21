.PHONY: docker run test

docker:
	docker build -t chromedriver --network host docker

run:
	docker run -it --rm --network host chromedriver bash

test:
	docker run -v $(PWD)/test:/test -it --rm --network host chromedriver python3 /test/test.py
