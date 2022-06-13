import numpy as np

igni_load = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
             100, 120, 140, 160, 180, 200, 220, 240, 260]
igni_rpm = [0, 500, 750, 1000, 1250,  1500, 1750,  2000, 2500, 3000, 3500,
            4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 11000]
spark_angle = np.array([(5, 5, 5, 5, 5, 11, 15, 6, 3, 2, -1, -2, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, 8, 10, 13, 16, 6, 3, 2, -1, -2, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, 8, 10, 14, 16, 10, 6, 2, -2, -3, -5, -8, -10, -10, -10, -10, -10), (5, 5, 5, -5, -5, 0, 0, 5, 8, 7, 7, 4, 1, -3, -6, -10, -10, -10, -10), (8, 8, 5, -5, -5, -5, -5, -5, 5, 9, 8, 4, 2, -1, -4, -7, -10, -10, -10), (13, 13, 5, -5, -5, -5, -5, -5, 5, 14, 12, 10, 7, 4, 1, -2, -5, -8, -10), (18, 18, 5, -5, -5, -5, -5, -5, 5, 17, 14, 11, 8, 5, 2, -1, -4, -7, -9), (24, 24, 5, -5, -5, -5, -5, -5, 5, 20, 17, 12, 10, 7, 4, 1, -2, -5, -8), (24, 24, 5, -5, -5, -5, -5, -5, 5, 20, 20, 15, 9, 7, 4, 1, -2, -5, -8), (28, 28, 5, -5, -5, -5, -5, -5, 5, 26, 22, 18, 12, 7, 6, 5, 1, -2, -5), (28, 28, 5, 5, 5, 5, 5, 5, 5, 27, 25, 20, 15, 11, 8, 7, 5, 2, -1), (28, 28, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 15, 12, 9, 8, 7, 3, 0), (33, 33, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 16, 13, 10, 9, 6, 3, 0), (38, 38, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 16, 12, 11, 11, 8, 5, 2), (38, 38, 38, 38, 35, 32, 31, 30, 28, 27, 25, 20, 15, 13, 12, 11, 8, 5, 2), (38, 38, 38, 38, 35, 34, 32, 31, 30, 28, 26, 23, 18, 16, 16, 15, 12, 9, 6), (38, 38, 38, 38, 38, 37, 35, 34, 34, 32, 30, 27, 22, 20, 20, 17, 14, 11, 8), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10), (38, 38, 38, 38, 38, 37, 36, 35, 35, 34, 34, 31, 26, 25, 22, 19, 16, 13, 10)
                        ])
