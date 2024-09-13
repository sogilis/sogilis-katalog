#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <stdint.h>
#include <cmocka.h>

#include "led.h"

static void test_led_should_failed() {
    print_error("Need to implement led module !\r\n");
}

int main(void) {
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_led_should_failed),
    };

    return cmocka_run_group_tests(tests, NULL, NULL);
}
