import wave
import struct


def pitch_and_toss():
    with wave.open("in.wav", mode="rb") as source:
        data = struct.unpack("<" + str((frames_count := source.getnframes())) + "h",
                             source.readframes(frames_count))
        newdata = data[(len(data) // 4) * 2:(len(data) // 4) * 3] + data[(len(data) // 4) * 3:]\
            + data[:len(data) // 4] + data[len(data) // 4:(len(data) // 4) * 2]
        newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    with wave.open("out.wav", mode="wb") as dest:
        dest.setparams(source.getparams())
        dest.writeframes(newframes)
