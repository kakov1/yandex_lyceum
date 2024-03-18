def defractalize(fractal):
    for i in fractal:
        if not str(i).isalnum():
            count = 0
            for j in i:
                if j in fractal:
                    count += 1
            if count == len(i):
                del fractal[fractal.index(i)]
