namespace Parser.Tests
{
    using System.Collections.Generic;
    using Microsoft.VisualStudio.TestTools.UnitTesting;
    using SensorReadings;

    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            string hex = "03 67 01 10 05 67 00 FF".Replace(" ", "");

            IReadOnlyList<ISensorReading> list = SensorReadingParser.Parse(hex);

            Assert.IsInstanceOfType(list[0], typeof(TemperatureSensor));
            Assert.IsInstanceOfType(list[1], typeof(TemperatureSensor));

            var item0 = (TemperatureSensor) list[0];
            var item1 = (TemperatureSensor) list[1];

            Assert.AreEqual(3, item0.Channel);
            Assert.AreEqual(0x67, item0.Type);
            Assert.AreEqual(27.2m, item0.Temperature);

            Assert.AreEqual(5, item1.Channel);
            Assert.AreEqual(0x67, item1.Type);
            Assert.AreEqual(25.5m, item1.Temperature);
        }

        [TestMethod]
        public void TestMethod2()
        {
            string hex = "01 67 FF D7".Replace(" ", "");

            IReadOnlyList<ISensorReading> list = SensorReadingParser.Parse(hex);

            Assert.IsInstanceOfType(list[0], typeof(TemperatureSensor));

            var item0 = (TemperatureSensor) list[0];
            Assert.AreEqual(1, item0.Channel);
            Assert.AreEqual(0x67, item0.Type);
            Assert.AreEqual(-4.1m, item0.Temperature);
        }

        [TestMethod]
        public void TestMethod3()
        {
            string hex = "06 71 04 D2 FB 2E 00 00".Replace(" ", "");

            IReadOnlyList<ISensorReading> list = SensorReadingParser.Parse(hex);

            Assert.IsInstanceOfType(list[0], typeof(Accelerometer));
             var item0 = (Accelerometer) list[0];

            Assert.AreEqual(6, item0.Channel);
            Assert.AreEqual(0x71, item0.Type);
            Assert.AreEqual(1.234m, item0.X);
            Assert.AreEqual(-1.234m, item0.Y);
            Assert.AreEqual(0m, item0.Z);
        }

        [TestMethod]
        public void TestMethod4()
        {
            string hex = "01 88 06 76 5f f2 96 0a 00 03 e8".Replace(" ", "");

            IReadOnlyList<ISensorReading> list = SensorReadingParser.Parse(hex);

            Assert.IsInstanceOfType(list[0], typeof(GpsLocation));

            var item0 = (GpsLocation) list[0];

            Assert.AreEqual(1, item0.Channel);
            Assert.AreEqual(0x88, item0.Type);
            Assert.AreEqual(42.3519m, item0.Latitude);
            Assert.AreEqual(-87.9094m, item0.Longitude);
            Assert.AreEqual(10m, item0.Altitude);
        }
    }
}