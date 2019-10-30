using System;

namespace roman_numerals
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = -1;
            int i;
            while ((i = Console.Read()) != -1)
            {
                count++;
            }
            Console.WriteLine(count == 0 ? "" : count.ToString());
        }
    }
}
