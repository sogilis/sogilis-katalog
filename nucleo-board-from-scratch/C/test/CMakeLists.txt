# Test suite for Led
add_cmocka_test(test_led
    SOURCES led/test_led.c
    COMPILE_OPTIONS -DUTEST -std=c99 -Og -g -Wall -W -Wextra -Werror
    LINK_LIBRARIES cmocka-static led
)
