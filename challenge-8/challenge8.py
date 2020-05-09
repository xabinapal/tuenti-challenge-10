# pip install python-brainfuck

import brainfuck

with open("../assets/challenge-8/05-headache.png", "rb") as f:
    image_data = f.read()
    end_of_image = image_data.rindex(b"\n")
    brainfuck_code = image_data[end_of_image+1:].decode("ascii")
    brainfuck_func = brainfuck.to_function(brainfuck_code)
    result = brainfuck_func()
    print(result)