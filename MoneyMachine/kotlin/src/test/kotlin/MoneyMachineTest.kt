import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.ValueSource
import kotlin.test.Test
import kotlin.test.assertNotNull

class MoneyMachineTest {

    @Test
    fun `can create a money machine`() {
        assertNotNull(MoneyMachine())
    }
    
    @Test
    fun `idle display insert coins`()
    {
        val machine  = MoneyMachine()
        assert(machine.display() == "INSERT COINS")
    }
    
    @ParameterizedTest(name = "{displayName} [{0}]")
    @ValueSource(doubles = [0.1, 0.2, 0.5, 1.0, 2.0])
    fun `add a valid coin to the machine`(coin: Double) {
        val machine  = MoneyMachine()
        machine.add(coin)
        assert(machine.display() == "$coin €")
    }

    @Test
    fun `add 2 cents to the machine`() {
        val machine  = MoneyMachine()
        machine.add(0.02)
        assert(machine.display() == "INSERT COINS")
    }
    
    @Test
    fun `add 10 cents and 1€`() {
        val machine  = MoneyMachine()
        machine.add(0.1)
        machine.add(1.0)
        assert(machine.display() == "1.1 €")
    }
    
        @Test
    fun `add 10 cents and reject 2 cents`() {
        val machine  = MoneyMachine()
        machine.add(0.1)
        machine.add(0.02)
        assert(machine.display() == "0.1 €")
    }
    
    @Test
    fun `add invalid piece`() {
        val machine  = MoneyMachine()
        machine.add(1.1)
        assert(machine.display() == "INSERT COINS")
    }
}