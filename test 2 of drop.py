def main(full_path_to_file):
    if not path.exists(full_path_to_file):
        print("File does not exist", full_path_to_file)
        return None, None, None, None, None

    data = np.loadtxt(full_path_to_file, delimiter=",")
    force_plate = data[:, 8]
    sampling_rate = 1000

    baseline_length = int(0.2 * sampling_rate)
    baseline = np.mean(force_plate[:baseline_length])

    delta = 5
    force_plate_list = force_plate.tolist()

    first_landing_index = -1
    for index in range(baseline_length, len(force_plate_list)):
        value = force_plate_list[index]
        if value > baseline + delta:
            first_landing_index = index
            break

    take_off_index = -1
    for index in range(first_landing_index + 10, len(force_plate_list)):
        value = force_plate_list[index]
        if value < baseline + delta:
            take_off_index = index
            break

    second_landing_index = -1
    for index in range(take_off_index + 10, len(force_plate_list)):
        value = force_plate_list[index]
        if value > baseline + delta:
            second_landing_index = index
            break

    time_of_contact = (take_off_index - first_landing_index) / sampling_rate
    time_of_flight = (second_landing_index - take_off_index) / sampling_rate

    g = constants.g
    RSI = (g * time_of_flight**2) / (8 * time_of_contact)

    signal = force_plate - baseline
    return signal, first_landing_index, take_off_index, second_landing_index, RSI