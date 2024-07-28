#!/usr/bin/env python


DEBUG = True

def convert_speed_to_meters_per_second(s_speed_unit, f_speed):
    """ Convert speed to meters per second """
    if s_speed_unit == 'MS':
        # 1 MS == 1 MS
        return f_speed
    elif s_speed_unit == 'MH':
        # 1 MH == 0.000278 MS
        f_meter_second = f_speed / 60 / 60
        return f_meter_second
    elif s_speed_unit == 'KMS':
        # 1 KMS == 1_000 MS
        f_meter_second = f_speed * 1_000
        return f_meter_second 
    elif s_speed_unit == 'KMH':
        # 1 KMH == 0.278 MS
        f_meter_second = f_speed * 1_000 / 60 / 60
        return f_meter_second
    else:
        print('ERROR: No matching speed unit!')
        exit(1)


def convert_distance_to_meters(s_distance_unit, f_distance):
    """ Convert distance to meters """
    if s_distance_unit == 'M':
        # 1 M == 1 M
        return f_distance
    elif s_distance_unit == 'KM':
        # 1 KM == 1_000 M
        f_distance_meters = f_distance * 1_000
        return f_distance_meters
    elif s_distance_unit == 'AU':
        # 1 AU == 149_597_870_700 M
        f_distance_meters = f_distance * 149_597_870_700
        return f_distance_meters
    elif s_distance_unit == 'LY':
        # 1 LY == 9_460_730_472_580_800 M
        f_distance_meters = f_distance * 9_460_730_472_580_800
        return f_distance_meters
    else:
        print('ERROR: No matching distance unit!')
        exit(1)


def extract_time(f_time_in_seconds):
    # 
    pass


# function for calculating the time for a given distance and speed 
def calculate_time(s_distance_unit, s_speed_unit, f_distance, f_average_speed):
    """ 
        Function to calculate the time needed to clear a given distance 
        within a given speed 
    """
    # convert distance to meters
    f_distance_in_meters = convert_distance_to_meters(s_distance_unit, f_distance)

    # convert speed to meters per second 
    f_speed_in_msec = convert_speed_to_meters_per_second(s_speed_unit, f_average_speed)

    # calculate needed time in seconds 
    f_time_in_sec = f_distance_in_meters / f_speed_in_msec

    # extract time 

    return f_time_in_sec


# ask for distance type 
print('[Units of distance: M, KM, AU, LY]')
s_distance_unit = input('Enter unit of distance: ').upper()

# ask for distance 
f_distance = float(input('Enter distance: '))

# ask for unit of speed 
print('[Units of speed: MS, MH, KMS, KMH]')
s_speed_unit = input('Enter unit of speed: ').upper()

# ask for average speed 
f_average_speed = float(input('Enter average speed: '))


if DEBUG:
    print(f"\nDistance Unit: {s_distance_unit}")
    print(f"Distance:      {f_distance}")
    print(f"Speed Unit:    {s_speed_unit}")
    print(f"Average Speed: {f_average_speed}\n")


f_result = calculate_time(s_distance_unit, s_speed_unit, f_distance, f_average_speed)

f_time_in_hours = f_result / 60 / 60

print(f"Estimated arrival in {f_result} seconds.\n")
print(f"Estimated arrival in {f_time_in_hours} hours.\n")

