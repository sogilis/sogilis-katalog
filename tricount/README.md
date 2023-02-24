# Tricount Kata

Good accounts make good friends : build a replica of the infamous [tricount application](https://www.tricount.com/fr/faire-les-comptes-entre-amis).

## Problem specification

tricounts.json has some input samples, solutions.json holds the corresponding solutions. They may be usefull resources for your first test cases ;)

Format explanation (feel free to make your own representation of the problem as your application evolves):

Consider an entry in "tricounts.json":
```
{
	"id": "AB-A_B",
	"users": ["Alice", "Bob"],
	"expanses": [
		{ "from": "A", "to": ["B"], "amount": 1.0 },
	]
}
```
It means "Alice advanced 1.0 to Bob"
The corresponding solution in "solutions.json" is:
```
{
	"id": "AB-A_B",
	"refunds": [ { "from": "Bob", "to": "Alice", "amount": 1.0 }]
}
```
Which means "Bob must give Alice 1.0 to solve all the debts of this tricount"

Let's see a more complex example :
```
	{
		"id": "ABC-A_BC-A_C",
		"users": ["Alice", "Bob", "Charlie"],
		"expanses": [
			{ "from": "Alice", "to": ["Alice", "Bob", "Charlie"], "amount": 3.0 },
			{ "from": "Alice", "to": ["Alice", "Charlie"], "amount": 2.0 },
		]
	}
```
Means "Alice paid 3.0 for everyone (a pizza for example), and 2.0 for her and Charlie (she also paid for two ice-creams but Bob didn't like ice-cream)"

The corresponding solution is :
```
	{
		"id": "ABC-A_BC-A_C",
		"refunds": [ { "from": "Bob", "to": "Alice", "amount": 1.0 }, { "from": "Charlie", "to": "Alice", "amount": 2.0 }]
	}
```
Which means "Bob must give alice 1.0 and Charlie must give Alice 2.0 to solve all the debts"
