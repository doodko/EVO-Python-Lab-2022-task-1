def direction(facing, turn):
    compass = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    try:
        new_position = (compass.index(facing) + turn // 45) % 8
        answer = compass[new_position]
        
    except ValueError:
        answer = f"No such direction as {facing}, please use one of {compass}."
    except TypeError:
        answer = f"Please use a valid integer instead of {turn}."

    return answer
