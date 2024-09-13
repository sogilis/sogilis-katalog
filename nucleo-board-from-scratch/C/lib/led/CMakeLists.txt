set(LIB_TARGET led)

add_library(${LIB_TARGET} STATIC)

target_sources(${LIB_TARGET} PRIVATE led.c)

target_include_directories(${LIB_TARGET} INTERFACE .)

target_compile_options(${LIB_TARGET} PRIVATE $<$<CONFIG:test>:-DUTEST> -W -Wall -Wextra -Werror)
