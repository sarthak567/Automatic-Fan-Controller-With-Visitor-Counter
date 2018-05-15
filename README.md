# Automatic fan controller with visitor counter 

Requirements - 

              1. Arduino UNO
              2. IR sensor 
              3. LM35 Temperature Sensor
              4. Breadboard
              5. Connecting wires
              
Objective - 

    Objective is ‘Optimum energy management’ by ensuring to switch on/off the fan depending on the surrounding
    temperature and presence of people in a room.

Working -
  
    LM35 sensor gives analog values and it is converted to digital value using AD converter of Arduino uno. 
    2 IR sensors are used (one for entry and one for exit).When someone enters into the room, the IR sensor detects
    it and visitor counter is incremented. If someone is present in the room and temperature is more than certain 
    threshold value, then the fan is automatically switched on. If the counter becomes 0, then the fan is 
    automatically switched off even if the temperature is high.
