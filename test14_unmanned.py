"""
Determine how long it will take the car to reach the end of the road
"""

def Unmanned(road: int, lights: int, track: list) -> int:
    """
    :param road: road length.
    :param lights: number of traffic lights.
    :param track: [0] - traffic light start
                  [1] - red light, seconds
                  [2] - green light, seconds
    :return: travel time
    """
    dist = 0
    time = 0
    # The loop runs until it completes road.
    while dist < road:
        for i in range(lights):
            if dist == track[i][0]:
                # If the remainder of the division of time and the sum of
                # lights is less than the time of red, then red.
                while time % (track[i][1]+track[i][2]) < track[i][1]:
                    time += 1
        time += 1
        dist += 1

    return time
