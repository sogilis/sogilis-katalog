package com.sogilis.katalog.romanNumerals;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.RegisterExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AppTest {

    @RegisterExtension
    static SystemExtension system = new SystemExtension();

    @Test
    void empty() {
        system.provideInputLine("");
        App.main(new String[]{});
        assertEquals("", system.getOutput());
    }

    @Test
    void one() {
        system.provideInputLine("I");
        App.main(new String[]{});
        assertEquals("1", system.getOutput());
    }

    @Test
    void two() {
        system.provideInputLine("II");
        App.main(new String[]{});
        assertEquals("2", system.getOutput());
    }

    @Test
    void three() {
        system.provideInputLine("III");
        App.main(new String[]{});
        assertEquals("3", system.getOutput());
    }

    @Test
    void four() {
        system.provideInputLine("IIII");
        App.main(new String[]{});
        assertEquals("4", system.getOutput());
    }
}
