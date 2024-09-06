namespace App
{
    public class RomanNumerals
    {
        public static void Main(string[] args)
        {
            int count = -1;
            int x;
            do
            {
                x = Console.Read();
                count += 1;
            } while (x != -1);

            if (count != 0)
            {
                Console.Write(count);
            }
        }
    }
}
