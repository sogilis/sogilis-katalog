cmake_minimum_required(VERSION 3.20)
project(led_driver CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(BUILD_SHARED_LIBS ON)

include(FetchContent)

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
	GIT_TAG v1.15.2
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)

FetchContent_MakeAvailable(googletest)

enable_testing()

add_library(ledDriver
    src/ledDriver.cpp
)

target_include_directories(ledDriver PUBLIC
    inc
)

add_executable(test_ledDriver)

target_sources(test_ledDriver PRIVATE
    test/test_ledDriver.cpp
)

target_link_libraries(test_ledDriver PRIVATE
    ledDriver
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(test_ledDriver)