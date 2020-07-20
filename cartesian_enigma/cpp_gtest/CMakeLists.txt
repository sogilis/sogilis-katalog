cmake_minimum_required(VERSION 3.0)

project(decoder)

set(SOURCES decoder.cpp)
set(MAIN main.cpp)
set(HEADERS decoder.hpp)

add_subdirectory("googletest-release-1.10.0/googletest")

add_executable(${PROJECT_NAME} ${MAIN} ${SOURCES} ${HEADERS})

set(TESTS unit_tests.cpp)

add_executable(unit_tests ${TESTS} ${SOURCES})
target_link_libraries(unit_tests gtest_main)
