def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center'] - 0.2;
    steering = abs(params['steering_angle'])
    off_track = params['is_offtrack']
    is_reversed = params['is_reversed']
    left = params['is_left_of_center']
    speed = params['']

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    # marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if not left:
        reward = 0.2
    else:
        if distance_from_center > marker_2:
            reward = 1.25
        elif distance_from_center > marker_1:
            reward = 1.15
        else:
            reward = 1


    if off_track:
        reward = 1e-3

    if is_reversed:
        reward = 1e-3

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8


    return float(reward)
