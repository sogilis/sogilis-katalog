using System;

namespace roman_numerals
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(new RomanNumeral(Console.ReadLine()).ToDecimal());
        }
    }
}
