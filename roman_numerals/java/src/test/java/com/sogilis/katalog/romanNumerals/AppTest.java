package com.sogilis.katalog.romanNumerals;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.RegisterExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AppTest {

    @Test
    void empty() {
        assertEquals(null, App.convert(""));
    }

    @Test
    void one() {
        assertEquals(1, App.convert("I"));
    }

    @Test
    void two() {
        assertEquals(2, App.convert("II"));
    }

    @Test
    void three() {
        assertEquals(3, App.convert("III"));
    }

    @Test
    void four() {
        assertEquals(4, App.convert("IIII"));
    }
}
