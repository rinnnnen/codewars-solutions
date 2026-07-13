def remove_noise(st):
    noise = '%$&/#·@|º\ª'
    return st.translate(str.maketrans('', '', noise))
