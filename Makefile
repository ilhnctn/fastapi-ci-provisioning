CURRENT_DIRECTORY := $(shell pwd)

help:
	@echo "=========== Welcome to MB-Case makefile Help ==========="
	@echo "=========== Example usages are as below.     ==========="
	@echo "make IMAGE_TAG=123.. run	=> To start docker run -p 8080:8080 $IMAGE_TAG"
	@echo "make CONTAINER=... tail  => Show container logs"

run:
	@docker run -p -e DATA_API_URL=${DATA_API_URL} -e SENTRY_DSN=${SENTRY_DSN} 8080:8080 ${IMAGE_TAG}

stop:
	@docker stop ${CONTAINER}

test:
	@pytest tests -x -vv

.PHONY: start stop test