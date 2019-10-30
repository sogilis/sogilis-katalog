namespace roman_numerals
{
    public class RomanNumeral
    {
        private string value;

        public RomanNumeral(string value)
        {
            this.value = value;
        }

        public string ToDecimal()
        {
            return this.value == "" ? "" : this.value.Length.ToString();
        }
    }
}
