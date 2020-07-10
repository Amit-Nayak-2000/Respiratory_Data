import matplotlib.pyplot as plt
import csv
import numpy as np

filename = 'Old_Physicstoolbox_data/gyroscope - Copy.csv'

def main():
    t = np.zeros(22001)
    wy = np.zeros(22001)
    dt = 0.0036
    n = len(t)

    t, wy = preprocess(t, wy, dt, n)
    F_sample = (n/(t[22000] - t[0]))

    fhat = np.fft.fft(wy, n)
    PSD = fhat * np.conj(fhat) / n
    freq = (1/(dt*n)) * np.arange(n)
    L = np.arange(1, np.floor(n/2), dtype='int')

    Low_cutoff, High_cutoff = 0.8, 2.5

    Filtered_signal, Filtered_spectrum = bandpass_ifft(fhat, Low_cutoff, High_cutoff, F_sample)

    plot(t, wy, freq, PSD, L, Filtered_signal)




def plot(t, signal, freq, PSD, L, ffilt):
    fig, axs = plt.subplots(3, 1)

    plt.sca(axs[0])
    plt.plot(t, signal, color='r', LineWidth=1.5, label='wy (rad/s)')
    plt.xlim(t[0], t[-1])
    plt.xlabel('Time (seconds)')
    plt.legend()

    plt.sca(axs[1])
    plt.plot(freq[L], PSD[L], color='c', LineWidth=1.5, label='PSD')
    plt.xlim(freq[L[0]], freq[L[-1]])
    plt.xlabel('Frequency (Hz)')
    plt.legend()

    plt.sca(axs[2])
    plt.plot(t, ffilt, color='g', LineWidth=1.5, label='filtered')
    plt.xlim(t[0], t[-1])
    plt.xlabel('time (s)')
    plt.legend()

    plt.show()

def preprocess(t, wy, dt, length):
    t = np.zeros(length)
    wy = np.zeros(length)
    index = 0

    with open(filename) as f:
        for x in f:
            if index == length:
                break
            x = x.split(',')
            if(x[0] == 'time'):
                continue
            # print(t[index -1], x[0])
            # if t[index-1] == float(x[0]) and index != 0:
            #     continue

            t[index] = float(x[0])
            wy[index] = float(x[2])
            index += 1

    return t, wy

def bandpass_ifft(x, Low_cutoff, High_cutoff, F_sample):
    M = x.size

    [Low_cutoff, High_cutoff, F_sample] = map(float, [Low_cutoff, High_cutoff, F_sample])

    # Convert cutoff frequencies into points on spectrum
    [Low_point, High_point] = map(lambda F: F / F_sample * M / 2,
                                  [Low_cutoff, High_cutoff])  # the division by 2 is because the spectrum is symmetric

    Filtered_spectrum = [x[i] if i >= Low_point and i <= High_point else 0.0 for i in range(M)]  # Filtering
    Filtered_signal = np.fft.ifft(Filtered_spectrum)  # Construct filtered signal
    return Filtered_signal, Filtered_spectrum


main()