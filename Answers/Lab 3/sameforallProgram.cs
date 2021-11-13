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

            //var app = new TTNApplication("balaapp2", "ttn-account-v2.13sg70NzdTkNNYQVNvGFGalygLfjqRIFadEzx5WDtrQ", "eu");
            var app = new TTNApplication("balalab3", "ttn-account-v2.hKlhIzZDNQALuouS9YU_7jcNmyQS70obLB-Ga1WETMs", "asia-se");
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
            //byte bTemp = Convert.ToByte(data, 32);
            //double doubleTemp = Convert.ToDouble(bTemp);
            //var doubleVal = BitConverter.Int64BitsToDouble(bTemp);
            //Console.WriteLine("HI");

            string result = data.Replace("-", "");
            Console.WriteLine(result);
            //string hexString = "43480170";

            string hex = result;
            byte[] raw = new byte[hex.Length / 2];
            for (int i = 0; i < raw.Length; i++)
            {
                // THEN DEPENDING ON ENDIANNESS
                raw[i] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
                // OR
                //raw[raw.Length - i - 1] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
            }
            float f = BitConverter.ToSingle(raw, 0);
            Console.WriteLine(f);
            uint v = BitConverter.ToUInt32(BitConverter.GetBytes(f), 0);
            Console.WriteLine(v);

            try
            {
                string[] hex1 = data.Split('-');
                string newv = " ";
                foreach (string hexa in hex1)
                {
                    int value = Convert.ToInt32(hexa, 16);
                    string val = char.ConvertFromUtf32(value);
                    newv += val;
                }
                Console.WriteLine($"The Decoded value is value is: {newv}");
            }
            catch (Exception ex) { Console.WriteLine(ex.Message); }

            try
            {

                var temperature = ((result[1] >> 4) | result[0]) / 2;
                var humidity = ((result[3] >> 4) | result[2]) / 2;
                var led = ((result[5] >> 4) | result[4]) / 2;

                Console.WriteLine($"The Decoded value is value is: { temperature}");
                Console.WriteLine($"The Decoded value is value is: { humidity}");
                Console.WriteLine($"The Decoded value is value is: { led}");
            }
            catch (Exception ex) { Console.WriteLine(ex.Message); }
        }
    }
}
//try
//{
  //  string[] hex = data.Split('-');
   // string newv = " ";
   // foreach (string hexa in hex)
   // {
    //    int value = Convert.ToInt32(hexa, 16);
    //    string val = char.ConvertFromUtf32(value);
    //    newv += val;
   // }
   // Console.WriteLine($"The Decoded value is value is: {newv}");
//}
//catch (Exception ex) { Console.WriteLine(ex.Message); }