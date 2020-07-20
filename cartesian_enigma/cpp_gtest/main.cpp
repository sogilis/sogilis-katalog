#include <iostream>
#include "decoder.hpp"

int main(int argc, char *argv[])
{
	std::string ciphertext;
	std::cin >> ciphertext;
	std::cout << decode(ciphertext) << std::endl;

	return 0;
}
