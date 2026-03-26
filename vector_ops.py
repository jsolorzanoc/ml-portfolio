import numpy as np
import matplotlib.pyplot as plt

def vector_angle(v,w):
    """
    Compute the angle between two vectors v and w.
    
    Parameters
    --------------
    v,w : np.ndarray
        Input vectors of the same shape.

    Returns
    --------------
    floats
        Angle in degrees
    """

    #Dot product v.w
    dot = np.dot(v,w)

    #Lenghts ||v|| and ||w|| 
    len_v = np.linalg.norm(v)
    len_w = np.linalg.norm(w)

    #Angle between them (v.w = ||u|| ||v|| cos 0)
    cos_theta = dot / (len_v * len_w) #calculation
    angle_rad = np.arccos(cos_theta) #calculation to randias
    angle_deg = np.degrees(angle_rad) #calculation to degrees (angle)

    print(f"u · v     = {dot}")
    print(f"||v||     ={len_v:.4f}")
    print(f"||w||     = {len_w:.4f}")
    print(f"Angle     = {angle_deg:.2f}°")
    return angle_deg

#Define vectors
v = np.array([3, 1])
w = np.array([1, 2])
#compute angle
result = vector_angle(v,w)

#Plot
fig, ax = plt.subplots()
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v= [3,1]')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label=' w= [1,2]')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title(f"Angle between v and w = {result:.2f}°")

plt.show()












