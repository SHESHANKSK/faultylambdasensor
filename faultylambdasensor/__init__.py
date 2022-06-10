from fulemap import fuleMap
import json
from ignitionmap import ignition_maps
fulemap = fuleMap
for engineModel, load, rpm, afr in fulemap.items():
    if engineModel == "YAHAMA":
        print(load)
        print(rpm)
        print(afr)


def airfuleratio():
    pass


def sparkangle():
    pass
