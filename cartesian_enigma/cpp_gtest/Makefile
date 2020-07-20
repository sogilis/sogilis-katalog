BUILD_DIR=build
PROJECT_NAME=decoder
UNIT_TESTS_NAME=unit_tests

SOURCES=$(wildcard *.cpp)
HEADERS=$(wildcard *.hpp)

.PHONY: build run get_gtest test

all: build

$(BUILD_DIR)/$(UNIT_TESTS_NAME): $(SOURCES) $(HEADERS)
	mkdir -p $(BUILD_DIR)
	cmake -B $(BUILD_DIR) .
	make -C $(BUILD_DIR)

$(BUILD_DIR)/$(PROJECT_NAME): $(SOURCES) $(HEADERS)
	mkdir -p $(BUILD_DIR)
	cmake -B $(BUILD_DIR) .
	make -C $(BUILD_DIR)

build: $(BUILD_DIR)/$(PROJECT_NAME)

run:
	./$(BUILD_DIR)/$(PROJECT_NAME)

get_gtest:
	wget https://github.com/google/googletest/archive/release-1.10.0.tar.gz
	tar -xvzf release-1.10.0.tar.gz
	rm release-1.10.0.tar.gz

test: $(BUILD_DIR)/$(UNIT_TESTS_NAME)
	./$(BUILD_DIR)/$(UNIT_TESTS_NAME)

clean:
	rm -rf $(BUILD_DIR)
	rm -rf release-1.10.0.tar.gz
	rm -rf googletest-release-1.10.0
