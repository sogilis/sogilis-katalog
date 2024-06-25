#include <stdarg.h>
#include <stddef.h>
#include <stdint.h>
#include <setjmp.h>
#include <cmocka.h>

#include <ledDriver.h>

static void test_should_failed(void **state) {
    fail_msg("Kata is empty :)");
}

int main(void) {
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_should_failed),
    };

    return cmocka_run_group_tests(tests, NULL, NULL);
}