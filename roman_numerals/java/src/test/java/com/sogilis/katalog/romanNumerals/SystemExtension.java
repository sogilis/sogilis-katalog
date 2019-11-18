package com.sogilis.katalog.romanNumerals;

import org.junit.jupiter.api.extension.AfterEachCallback;
import org.junit.jupiter.api.extension.BeforeEachCallback;
import org.junit.jupiter.api.extension.ExtensionContext;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

/**
 * This extension stubs System.in and System.out.
 */
public class SystemExtension implements BeforeEachCallback, AfterEachCallback {
    private final InputStream systemIn = System.in;
    private final PrintStream systemOut = System.out;

    private ByteArrayOutputStream systemOutStub;

    @Override
    public void beforeEach(final ExtensionContext context) throws Exception {
        systemOutStub = new ByteArrayOutputStream();
        System.setOut(new PrintStream(systemOutStub));
    }

    @Override
    public void afterEach(final ExtensionContext context) throws Exception {
        System.setIn(systemIn);
        System.setOut(systemOut);
    }

    public void provideInputLine(String input) {
        final ByteArrayInputStream systemInStub = new ByteArrayInputStream((input + "\n").getBytes());
        System.setIn(systemInStub);
    }

    public String getOutput() {
        return systemOutStub.toString().replaceFirst("\\s$","");
    }
}
