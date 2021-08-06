GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
BINARY_NAME=gol
BUILD_DIR=build

.DEFAULT_GOAL := run
.PHONY: all run build clean-build clean test
build:
	$(GOBUILD) -o $(BUILD_DIR)/$(BINARY_NAME)

clean:
	$(GOCLEAN)
	rm -f $(BUILD_DIR)/$(BINARY_NAME)

clean-build: clean build

test:
	$(GOTEST)

run: build
	./$(BUILD_DIR)/$(BINARY_NAME)