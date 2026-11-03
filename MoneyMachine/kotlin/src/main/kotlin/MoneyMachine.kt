class MoneyMachine {
    
    var total = 0.0
    val validCoins = listOf(0.1,0.2,0.5,1.0,2.0)
    
    fun add(coin: Double) {
        if (validCoins.contains(coin)) {
            total += coin
        }
    }
    
    fun display(): String {
        return if (total == 0.0) {
            "INSERT COINS"    
        } else {
            "$total €"  
        }
    }
}