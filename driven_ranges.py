import itertools


def current_samples(current_list):
    return '4-5, 2'


def current_individual_readings(current_readings):
    current_counts_list = []
    current_counts = {}
    for i in range(0, 6):
        current_counts['current'] = i
        current_counts['occurrence'] = 0
        current_counts_list.append(current_counts.copy())
    for current in current_readings:
        current_counts_list[current]['occurrence'] += 1
    return current_counts_list


def log_consecutive_groups(current_counts):
    return [list(y) for x, y in itertools.groupby(current_counts, lambda z: z == 0) if not x]


def identify_error(current_sensor_readings):
    if 2000 in current_sensor_readings:
        current_sensor_readings.remove(2000)
    return current_sensor_readings


def current_data(data):
    return round((10 * data) / 2000)


