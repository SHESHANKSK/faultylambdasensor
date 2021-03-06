# faultylambdasensor
>Python Package for determining the Air:Fuel Ratio, Lambda Value from the Fuel Maps and Spark Angle from the Ignition Map.

## Introduction
An exhaust gas oxygen sensor, also known as lambda sensor, is a device for measuring the oxygen proportion in the exhaust gas being analyzed. The sensor is part of the emissions control system and provides data to the engine management computer. The input from the oxygen sensor is used to balance the fuel mixture. It was developed by the Robert Bosch company in the 1960's. This sensor enables the engine to run as efficiently as possible and also reduce exhaust emissions. The exhaust oxygen sensor includes a sensing portion that is exposed to the exhaust gas stream to detect residual oxygen in the exhaust gas and transmit the data to the control unit. A control unit fine-tunes the electric pulses transmitted to the fuel injectors. It includes a zirconia ceramic tube that is covered by a louvred metal shroud to protect it from breaking. A wire contacts the inner surface of the tube through a spring and an electrode bush. The inner and outer surfaces of the tube are covered with a porous platinum layer, which makes the tube act as a porous, solid electrolyte. The tube becomes a conductor at temperatures around 350°C, and detects the oxygen level in exhaust gas by creating a voltage.

## Applications
- The exhaust oxygen sensors are used in determining if the air-fuel mixture is rich or lean. 
- Modern park-ignited combustion engines employ oxygen sensors and catalytic converters to ensure that engines burn their fuel efficiently and cleanly in order to reduce exhaust emissions. 
- Thus, these sensors also help in reducing the amounts of both unburnt fuel and oxides of nitrogen entering the atmosphere.
- Since oxygen sensors are located in the exhaust stream, they do not measure the amount of air or the fuel entering the engine directly. 
- However, when information from oxygen sensors is combined with information from other sources, it can be used to indirectly determine the air-fuel ratio.

## Features
- Calculate the Air:Fuel Ratio
- Calculate the Lambda Value
- Calcuate the Spark Angle of the Engine

## Support
- Cross Platform Support for all OS

## Examples
### Installation
```cmd
pip install faultylambdasensor
```
### Calculating the Air:Fuel Ratio
```py
from faultylambdasensor import FLS
afr = FLS.airfuelratio(load=150, rpm=1500)
print(afr)
```

### Calculating the Lambda Value
```py
from faultylambdasensor import FLS
l_v = FLS.lambdavalue(load=150, rpm=1500)
print(l_v)
```

### Calculating the Spark Angle
```py
from faultylambdasensor import FLS
s_a = FLS.sparkangle(load=150, rpm=1500)
print(s_a)
```

## Contributing to faultylambdasensor

### Todos
- [x] Code Completion

- [ ] Add Standard Documentation (Mk Docs)

- [ ] Add Fuel Maps and Ignition Maps of All avaliable Engines

- [ ] Replace the interp2d scipy function with custom one to replace the overall package size

## Code of Conduct

Everyone interacting in the **faultylambdasensor** project's codebases, issue trackers, and
discussion forums is expected to follow the [PyPA Code of Conduct].


## License

[MIT License](https://github.com/SHESHANKSK/faultylambdasensor/blob/main/LICENSE)
