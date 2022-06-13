from fulemap import fule_load, fule_rpm, afr
from ignitionmap import igni_load, igni_rpm, spark_angle
from scipy.interpolate import interp2d


def airfuleratio(given_load, given_rpm):
    a_f_r = interp2d(fule_load, fule_rpm, afr, kind='linear', fill_value='-1')
    airistofuleratio = float(round(a_f_r(given_load, given_rpm)[0], 4))/14.7
    return airistofuleratio


def sparkangle(given_load, given_rpm):
    spang = interp2d(igni_load, igni_rpm, spark_angle,
                     kind='linear', fill_value='-1')
    sparkangle = float(round(spang(given_load, given_rpm)[0], 4))
    return sparkangle
