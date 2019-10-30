using System;

class Program
{
    static void Main()
    {
        int count = -1;
        while (Console.Read() != -1)
        {
            count++;
        }
        if(count > 0)
        {
            Console.WriteLine(count);
        }
    }
}
