using App;
using System;
using System.IO;
using Xunit;

public class RomanNumeralsTest : IDisposable
{
    private readonly TextReader originalInput;
    private readonly TextWriter originalOutput;
    private readonly StringWriter output = new StringWriter();

    public RomanNumeralsTest()
    {
        originalInput = Console.In;
        originalOutput = Console.Out;
        Console.SetOut(output);
    }

    public void SetInput(String input)
    {
        Console.SetIn(new StringReader(input));
    }

    public String GetOutput()
    {
        return output.ToString();
    }

    public void Dispose()
    {
        Console.SetIn(originalInput);
        Console.SetOut(originalOutput);
    }


    [Fact]
    public void Empty()
    {
        SetInput("");
        RomanNumerals.Main(new string[] { });
        Assert.Equal("", GetOutput());
    }

    [Fact]
    public void One()
    {
        SetInput("I");
        RomanNumerals.Main(new string[] { });
        Assert.Equal("1", GetOutput());
    }

    [Fact]
    public void Two()
    {
        SetInput("II");
        RomanNumerals.Main(new string[] { });
        Assert.Equal("2", GetOutput());
    }

    [Fact]
    public void Three()
    {
        SetInput("III");
        RomanNumerals.Main(new string[] { });
        Assert.Equal("3", GetOutput());
    }
}
