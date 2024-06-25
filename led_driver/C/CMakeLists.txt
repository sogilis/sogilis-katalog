cmake_minimum_required(VERSION 3.20)
project(led_driver C)

include(FetchContent)

FetchContent_Declare(
    cmocka
    GIT_REPOSITORY https://git.cryptomilk.org/projects/cmocka.git
    GIT_TAG        cmocka-1.1.7
    GIT_SHALLOW    1
)

set(WITH_STATIC_LIB ON CACHE BOOL "CMocka: Build with a static library" FORCE)
set(WITH_CMOCKERY_SUPPORT OFF CACHE BOOL "CMocka: Install a cmockery header" FORCE)
set(WITH_EXAMPLES OFF CACHE BOOL "CMocka: Build examples" FORCE)
set(UNIT_TESTING OFF CACHE BOOL "CMocka: Build with unit testing" FORCE)
set(PICKY_DEVELOPER OFF CACHE BOOL "CMocka: Build with picky developer flags" FORCE)

FetchContent_MakeAvailable(cmocka)

enable_testing()

add_library(ledDriver src/ledDriver.c)

target_include_directories(ledDriver PUBLIC inc)

add_executable(test_ledDriver test/test_ledDriver.c)
target_link_libraries(test_ledDriver ledDriver cmocka)

add_test(NAME test_ledDriver COMMAND test_ledDriver)