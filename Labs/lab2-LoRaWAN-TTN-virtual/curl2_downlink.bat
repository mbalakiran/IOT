rem 
rem https://www.thethingsnetwork.org/forum/t/using-curl-or-postman-for-the-http-integration-on-windows/12467
rem
curl -X POST -v -d "{\"dev_id\":\"node\",\"payload_raw\":\"AQE=\"}" [url to your TTN integration]
rem
rem curl -X POST -v -d "{\"dev_id\":\"node\",\"port\":15,\"payload_raw\":\"AQE=\"}" [url to your TTN integration]
rem
pause