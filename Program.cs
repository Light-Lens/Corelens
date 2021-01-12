using System;
using System.IO;

namespace Corelens
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Corelens";
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.Clear();
            Console.WriteLine("Corelens");
            string[] Colors = {
            "1 ->       System scan",
            "2 ->       Custom scan"
            };
            for (int i = 0; i < Colors.Length; i++)
            {
                Console.WriteLine(Colors[i]);
            }
            Console.Write("\nEnter the number> ");
            ConsoleKeyInfo Control = Console.ReadKey();
            string GetKey = Control.Key.ToString();
            Console.WriteLine("");
            if (GetKey == "D1")
            {
                string WinDir = Path.GetPathRoot(Environment.SystemDirectory);
            }

            else if (GetKey == "D2")
            {
                // code here.
            }

            else Console.WriteLine($"Cannot find any feature for {GetKey}!");
        }
    }
}
