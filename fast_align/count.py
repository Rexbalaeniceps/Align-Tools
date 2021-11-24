def mapping(file, output):
    text = []
    with open(file, "r", encoding="utf-8") as f:
        content = f.readlines()

    length = len(content)

    for i in range(length):
        text.append(content[i].split())

    mappings = {}

    for i in range(length):
        for j in range(len(text[i])):
            for k in range(len(text[i][j])):
                if text[i][j][k] == "-":
                    key = text[i][j][:k]
                    value = text[i][j][k+1:]
                    break
            if key not in mappings.keys():
                mappings[key] = [value, ]
            elif value not in mappings[key]:
                mappings[key].append(value)

    with open(output, "w", encoding="utf-8") as f:
        for key, value in mappings.items():
            f.write(str(key) + str(value) + "\n")


mapping(file=r"/data1/wbxu/fast_align_res/token_source-target.align", output=r"/data1/wbxu/fast_align_res/source-target_count.align")
mapping(file=r"/data1/wbxu/fast_align_res/token_target-source.align", output=r"/data1/wbxu/fast_align_res/target-source_count.align")