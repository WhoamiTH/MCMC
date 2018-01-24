import numpy as np
matrix = np.matrix([[0.9,0.075,0.025],
                    [0.15,0.8,0.05],
                    [0.25,0.25,0.5]], dtype=float)
vector = np.matrix([0.2,0.6,0.2],dtype=float)
# vector = np.matrix([[0.3,0.4,0.3]], dtype=float)
for i in range(100):
    vector = vector*matrix
    print("Current round:" , i+1)
    print(vector)
#
# import numpy as np
# matrix = np.matrix([[0.625, 0.3125, 0.0625],
#                     [0.625, 0.3125, 0.0625],
#                     [0.625, 0.3125, 0.0625]], dtype=float)
# vector = np.matrix([0.625,0.3125,0.0625],dtype=float)
# # vector = np.matrix([[0.3,0.4,0.3]], dtype=float)
# for i in range(100):
#     vector = vector*matrix
#     print("Current round:" , i+1)
#     print(vector)