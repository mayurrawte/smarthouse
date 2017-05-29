
-- Connection
device_id = 'bf943243a95f47f28484ff4a9778dfaa'


gpio.mode(6,gpio.OUTPUT)
gpio.mode(8,gpio.OUTPUT)
gpio.mode(1,gpio.OUTPUT)
gpio.mode(7,gpio.OUTPUT)


cntr = function()
    print("Moister Sensor ")
    moisture = adc.read(0)
    print(moisture)
    print("tempature")
    status, temp, humi, temp_dec, humi_dec = dht.read(2)    
    print("DHT Temperature:"..temp..";".."Humidity:"..humi)
    if(moisture > 750) then
        gpio.write(7,gpio.HIGH)
    else
        gpio.write(7,gpio.LOW)
    end
    if(humi > 40) then
        gpio.write(1,gpio.HIGH)
        gpio.write(6,gpio.LOW)
    elseif(humi < 40 and humi > 20) then
        gpio.write(1,gpio.LOW)
        gpio.write(6,gpio.LOW)
    elseif (humi < 20) then
        gpio.write(6,gpio.HIGH)
        gpio.write(1,gpio.LOW)
    end

    ht = gpio.read(6)
    fn = gpio.read(1)
    wp = gpio.read(7)

    
    
    data = {}
    data['humi'] = humi
    data['temp'] = temp
    data['moist'] = moisture
    data['ht'] = ht
    data['fn'] = fn
    data['wp'] = wp
    datajson = cjson.encode(data)
    if(conn) then
    pub("smarthouse112/update/"..device_id,datajson)
    end
 end



if(conn) then
    sub = function(topic)
            print("Connected")
           end
    pub = function(topic,msg)
                m:publish(topic,msg,0,0, function(client) print("sent") end)
            end
    m = mqtt.Client("clientid", 120)
    m:lwt("/lwt", "offline", 0, 0)
    m:on("connect", sub)
    m:on("offline", function(client) print ("offline") end)
    m:on("message", function(client, topic, data) 
      print(topic .. ":" ) 
      if data ~= nil then
        print(data)
      --  tb = cjson.decode(data)
        --for k,v in pairs(tb) do print(k,v)
          --  print(k..":"..v)
       -- end
        end
    end)
    -- for TLS: m:connect("192.168.11.118", secure-port, 1)
    m:connect("iot.eclipse.org", 1883, 0, sub,function(client, reason) print("failed reason: "..reason) end)
    m:close();
else
    print("Connection Error")
end

if(conn) then
mytimer = tmr.create()
mytimer:register(2000,tmr.ALARM_AUTO,cntr)
mytimer:start()
end
