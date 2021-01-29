


def wrap(string, max_width):
    result = " ".join(textwrap.wrap(string,max_width))
    return textwrap.fill(result,max_width)
    
