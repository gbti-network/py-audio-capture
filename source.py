import sounddevice as sd
import numpy as np
import wavio
import datetime

# Configuration for the recording
SAMPLE_RATE = 44100
CHANNELS = 2
DTYPE = np.int16
SECONDS_PER_CHUNK = 10  # You can modify this to record larger or smaller chunks at a time

def select_device():
    devices = sd.query_devices()
    input_devices = [device for device in devices if device['max_input_channels'] > 0]
    device_names = [device['name'] for device in input_devices]

    # Check for "Sound Mixer"
    for name in device_names:
        if "Sound Mixer" in name:
            return name

    # Check for "CABLE Output"
    for name in device_names:
        if "CABLE Output" in name:
            return name

    # If neither "Sound Mixer" nor "CABLE Output" is found, prompt for VB-Cable installation
    print("It seems you don't have a suitable input device installed.")
    print("Please consider downloading and installing VB-Cable for this purpose.")
    print("You can download it from here: https://vb-audio.com/Cable/")
    exit(1)

def get_filename_with_date_and_time():
    current_time = datetime.datetime.now()
    formatted_date_time = current_time.strftime('%m-%d-%Y_%H-%M-%S')
    filename = f"./output/recording_{formatted_date_time}.wav"
    return filename

def record_until_closed(device_name):
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=DTYPE, device=device_name) as stream:
        print("Recording... Press Ctrl+C to stop and save.")
        all_data = []

        try:
            while True:
                audio_chunk, _ = stream.read(int(SECONDS_PER_CHUNK * SAMPLE_RATE))
                all_data.append(audio_chunk)
        except KeyboardInterrupt:
            # If user presses Ctrl+C, stop recording and save to a WAV file
            print("Recording stopped. Saving...")

            # Concatenate all chunks to form the complete audio data
            audio_data = np.concatenate(all_data, axis=0)

            # Get filename with date and time
            filename = get_filename_with_date_and_time()

            # Save to a WAV file
            wavio.write(filename, audio_data, SAMPLE_RATE, sampwidth=2)
            print(f"Saved as '{filename}'")

if __name__ == "__main__":
    device_name = select_device()
    record_until_closed(device_name)
