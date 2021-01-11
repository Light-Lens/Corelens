using System;
using System.IO;

namespace Corelens
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Corelens";
            Console.WriteLine("Corelens");
            Console.Write("Enter your File path with it's name: ");
            string FilePath = Console.ReadLine();
            if (File.Exists(FilePath)) File.Delete(FilePath);
            else Console.WriteLine("Your requested file does not exist.");
        }
    }
}
