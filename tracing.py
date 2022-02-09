import numpy as np

def get_all_hits(sample_list,camera_list,sample_size):
    '''
    Return all hit points that on each sight ray with ascending distance order
    '''
    all_camera_hits = []
    # For every camera
    for camerapoint in camera_list:
        camera_hits = []
        # For every line points
        for endpoint in sample_list:
            line_hits = []
            # For every other sample points
            for spoint in sample_list:
                dist = point_distance_line(spoint,camerapoint,endpoint)
                if dist < sample_size:
                    line_hits.append([spoint,points_distance(spoint,camerapoint)])
            # Sort the line_hits with its points distance
            line_hits.sort(key=get_distance)
            camera_hits.append(line_hits)
        all_camera_hits.append(camera_hits)
    
    return all_camera_hits

def points_distance(p1,p2):
    return np.linalg.norm(p1-p2)

def get_distance(e):
    return e[1]

def point_distance_line(point,line_point1,line_point2):
    vec1 = line_point1 - point
    vec2 = line_point2 - point
    #print(np.abs(np.cross(vec1,vec2)),np.linalg.norm(line_point1-line_point2))
    distance = np.linalg.norm(np.cross(vec1,vec2)) / np.linalg.norm(line_point1-line_point2)
    #print(distance)
    return distance
    
def get_visible_percentage(camera_hits,sample_list):
    visiable_points = set()
    for i in range(len(camera_hits)):
        for j in range(len(camera_hits[i])):
            tup = tuple(camera_hits[i][j][0][0])
            if tup not in visiable_points:
                visiable_points.add(tup)
    return float(len(visiable_points)/len(sample_list))
