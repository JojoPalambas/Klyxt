def get_full_file(filename):
    f = open(filename, "r")
    ret = f.read()
    f.close()
    return ret

def story_blocks_from_string(text):
    blocks = text.split("\n===\n")

    sub_blocks = []
    for block in blocks:
        sub_blocks.append(block.split("\n"))

    ret = []
    for sub_block in sub_blocks:
        ret.append([sub_block[0], sub_block[1:]])

    return ret

def story_blocks_from_file(filename):
    return story_blocks_from_string(get_full_file(filename))