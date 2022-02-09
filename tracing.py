import numpy as np

def get_visiable_percentage(sample_list,camera_list,sample_size):
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
                    line_hits.append(spoint)
            camera_hits.append(line_hits)
        all_camera_hits.append(camera_hits)
    return all_camera_hits


def point_distance_line(point,line_point1,line_point2):
    vec1 = line_point1 - point
    vec2 = line_point2 - point
    #print(np.abs(np.cross(vec1,vec2)),np.linalg.norm(line_point1-line_point2))
    distance = np.linalg.norm(np.cross(vec1,vec2)) / np.linalg.norm(line_point1-line_point2)
    #print(distance)
    return distance
    