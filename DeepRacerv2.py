def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    left = params['is_left_of_center']
    speed = params['speed']
    
    reward = 0
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if left:
        reward += 0.3
    elif distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    # add speed penalty
    if speed < 1.0:
        reward *= 0.80
    else:
        reward += speed
    
    return float(reward)
