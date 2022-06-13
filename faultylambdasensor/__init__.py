#from fuelmap import fuel_load, fuel_rpm, afr
#from ignitionmap import igni_load, igni_rpm, spark_angle
from scipy.interpolate import interp2d
import numpy as np


fuel_load = [10, 20, 30, 40, 50, 60, 70, 80, 90,
             100, 120, 140, 160, 180, 200, 220, 240, 260]
fuel_rpm = [500, 1000, 1500, 2000, 2500, 3000, 3500,
            4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]
afr = np.array([(13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 12.0, 12.0, 11.7, 11.4, 11.1, 10.9, 10.6, 10.4, 10.2, 10.0), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 13.1, 13.1, 12.7, 12.4, 12.1, 11.8, 11.5, 11.2, 10.9, 10.7), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.1, 13.6, 12.7, 12.5, 12.4, 12.1, 11.8, 11.5, 11.2, 10.9), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.1,
                                                                                                                                                                                                                                                                                                                                                           13.6, 13.1, 12.6, 12.3, 12.1, 11.8, 11.1, 10.9, 10.6), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.3, 13.9, 13.6, 13.1, 12.8, 12.3, 11.9, 11.3, 10.8, 10.3), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.3, 14.0, 13.8, 12.4, 10.9, 10.1, 10.5, 10.3, 10.0, 9.7), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.3, 14.0, 13.1, 11.4, 9.7, 9.6, 9.6, 9.6, 9.6, 9.5), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 13.9, 13.3, 11.9, 10.8, 9.6, 9.6, 9.6, 9.6, 9.5, 9.5), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.0, 13.5, 13.2, 12.3, 11.4, 10.7, 9.6, 9.5, 9.5, 9.5, 9.4, 9.3), (14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.0, 13.5, 13.2, 12.3, 11.4, 10.7, 9.6, 9.5, 9.5, 9.5, 9.4, 9.3), (14.7, 14.7, 14.7, 14.7, 14.4, 13.8, 13.3, 12.4, 11.6, 11.3, 10.9, 10.4, 9.6, 9.5, 9.6, 9.6, 9.5, 9.5), (14.5, 14.5, 14.5, 14.5, 13.9, 13.3, 12.5, 11.5, 11.2, 11.1, 10.6, 10.2, 9.6, 9.6, 9.6, 9.6, 9.7, 9.6), (14.0, 14.0, 14.0, 14.0, 12.8, 12.5, 11.8, 11.1, 10.9, 10.8, 10.3, 10.3, 9.6, 9.7, 9.6, 9.6, 9.7, 9.6), (13.8, 13.8, 13.8, 13.1, 12.7, 11.8, 11.2, 11.1, 10.9, 10.8, 10.6, 10.5, 9.9, 10.0, 10.0, 10.0, 10.0, 10.0), (13.8, 13.8, 13.8, 13.1, 12.7, 11.8, 11.2, 11.1, 10.9, 10.8, 10.6, 10.6, 10.2, 10.3, 10.3, 10.2, 10.3, 10.2)
                ])

igni_load = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
             100, 120, 140, 160, 180, 200, 220, 240, 260]
igni_rpm = [0, 500, 750, 1000, 1250,  1500, 1750,  2000, 2500, 3000, 3500,
            4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 11000]
spark_angle = np.array([(5, 5, 5, 5, 5, 11, 15, 6, 3, 2, -1, -2, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, 8, 10, 13, 16, 6, 3, 2, -1, -2, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, 8, 10, 14, 16, 10, 6, 2, -2, -3, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, -5, -5, 0, 0, 5, 8, 7, 7, 4, 1, -3, -6, -10, -10, -10, -10), (8, 8, 5, -5, -5, -5, -5, -5, 5, 9, 8, 4, 2, -1, -4, -7, -10, -10, -10), (13, 13, 5, -5, -5, -5, -5, -5, 5, 14, 12, 10, 7, 4, 1, -2, -5, -8, -10), (18, 18, 5, -5, -5, -5, -5, -5, 5, 17, 14, 11, 8, 5, 2, -1, -4, -7, -9), (24, 24, 5, -5, -5, -5, -5, -5, 5, 20, 17, 12, 10, 7, 4, 1, -2, -5, -8), (24, 24, 5, -5, -5, -5, -5, -5, 5, 20, 20, 15, 9, 7, 4, 1, -2, -5, -8), (28, 28, 5, -5, -5, -5, -5, -5, 5, 26, 22, 18, 12, 7, 6, 5, 1, -2, -5), (28, 28, 5, 5, 5, 5, 5, 5, 5, 27, 25, 20, 15, 11, 8, 7, 5, 2, -1), (28, 28, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 15, 12, 9, 8, 7, 3, 0), (33, 33, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 16, 13, 10, 9, 6, 3, 0), (38, 38, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 16, 12, 11, 11, 8, 5, 2), (38, 38, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 15, 13, 12, 11, 8, 5, 2), (38, 38, 38, 38, 35, 34, 32, 31, 30, 28, 26, 23, 18, 16, 16, 15, 12, 9, 6), (38, 38, 38, 38, 38, 37, 35, 34, 34, 32, 30, 27, 22, 20, 20, 17, 14, 11, 8), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10)
                        ])


def airfuelratio(given_load, given_rpm):
    a_f_r = interp2d(fuel_load, fuel_rpm, afr, kind='linear', fill_value='-1')
    airistofuelratio = (float(round(a_f_r(given_load, given_rpm)[0], 4)))/14.7
    return airistofuelratio


def sparkangle(given_load, given_rpm):
    spang = interp2d(igni_load, igni_rpm, spark_angle,
                     kind='linear', fill_value='-1')
    sparkangle = float(round(spang(given_load, given_rpm)[0], 4))
    return sparkangle
