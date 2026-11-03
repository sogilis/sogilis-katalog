import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.ValueSource
import kotlin.test.Test
import kotlin.test.assertNotNull

class MoneyMachineTest {
    @Test
    fun `Ensure MoneyMachine obj is valid`(){
        assertNotNull(MoneyMachine())
    }
}