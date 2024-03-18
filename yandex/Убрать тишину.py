import wave
import struct


def break_the_silence():
    with wave.open("in.wav", mode="rb") as source:
        data = struct.unpack("<" + str((frames_count := source.getnframes())) + "h",
                             source.readframes(frames_count))
        newframes = struct.pack("<" + str(len((newdata := list(filter(
            lambda x: abs(x) > 5, data))))) + "h", *newdata)
    with wave.open("out.wav", mode="wb") as dest:
        dest.setparams(source.getparams())
        dest.writeframes(newframes)
