from fulemap import fule_load, fule_rpm, afr
from ignitionmap import igni_load, igni_rpm, spark_angle
from scipy.interpolate import interp2d


def airfuleratio(given_load, given_rpm):
    fu_car = interp2d(fule_load, fule_rpm, afr, kind='linear', fill_value='-1')
    y = float(round(fu_car(given_load, given_rpm)[0], 4))
    x = 14.7
    airistofuleratio = y/x
    return airistofuleratio


def sparkangle(given_load, given_rpm):
    fu_car = interp2d(igni_load, igni_rpm, spark_angle,
                      kind='linear', fill_value='-1')
    y = float(round(fu_car(given_load, given_rpm)[0], 4))
    x = 14.7
    sparkangle = y/x
    return sparkangle
