import wave
import struct


def chip_and_dale(number):
    with wave.open("in.wav", mode="rb") as source:
        data = struct.unpack("<" + str((frames_count := source.getnframes())) + "h",
                             source.readframes(frames_count))
        newframes = struct.pack("<" + str(len((newdata := data[::number]))) + "h", *newdata)
    with wave.open("out.wav", mode="wb") as dest:
        dest.setparams(source.getparams())
        dest.writeframes(newframes)
