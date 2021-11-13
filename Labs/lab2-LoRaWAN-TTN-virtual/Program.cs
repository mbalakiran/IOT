using ALoRa.Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ALoRa.ConsoleApp
{
    class Program
    {
      
        static void Main(string[] args)
        {
            Console.WriteLine("\nALoRa ConsoleApp - A The Things Network C# Library\n");

            var app = new TTNApplication("balaapp2", "ttn-account-v2.13sg70NzdTkNNYQVNvGFGalygLfjqRIFadEzx5WDtrQ", "eu");
            app.MessageReceived += App_MessageReceived;

            Console.WriteLine("Press return to exit!");
            Console.ReadLine();

            app.Dispose();

            Console.WriteLine("\nAloha, Goodbye, Vaarwel!");

            System.Threading.Thread.Sleep(1000);
        }

        private static void App_MessageReceived(TTNMessage obj)
        {
            var data = obj.Payload != null ? BitConverter.ToString(obj.Payload) : string.Empty;
            Console.WriteLine($"Message Timestamp: {obj.Timestamp}, Device: {obj.DeviceID}, Topic: {obj.Topic}, Payload: {data}");
            try
            { 
                string[] hex = data.Split('-');
                string newv = " ";
                foreach (string hexa in hex)
                {
                    int value = Convert.ToInt32(hexa, 16);
                    string val = char.ConvertFromUtf32(value);
                    newv += val;
                }
                Console.WriteLine($"The Decoded value is value is: {newv}");
            }
            catch (Exception ex) { Console.WriteLine(ex.Message); }
        }
    }
}