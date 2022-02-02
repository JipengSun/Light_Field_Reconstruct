import numpy as np
import math



def generate_points_array(offset_x,offset_y,offset_z,x_num,y_num,z_num,gap):
    xpos = generate_pos(offset_x,x_num,gap)
    ypos = generate_pos(offset_y,y_num,gap)
    zpos = generate_pos(offset_z,z_num,gap)
    #print(xpos)

    xv,yv,zv = np.meshgrid(xpos,ypos,zpos)
    #print(xv)

    return xv,yv,zv

def generate_pos(offset,num,gap):
    if num%2 == 0:
        pos = np.arange(offset-((num/2-0.5)*gap),offset+((num/2-0.5)*gap)+1,gap)
    else:
        pos = np.arange(offset-int((num-1)/2)*gap,offset+int((num-1)/2)*gap+1,gap)
    return pos

def get_angles(c_x,c_y,c_z):
    delta_az = math.atan2(c_y,c_x)*180.0/math.pi
    delta_el = math.atan2(c_z,c_x)*180.0/math.pi
    return delta_az,delta_el


