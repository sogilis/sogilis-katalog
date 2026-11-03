package moneymachine;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MoneyMachineTest {

    @Test
    void canCreateAMoneyMachine() {
        assertNotNull(new MoneyMachine());
    }
}
