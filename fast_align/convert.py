def recover_forward(path1, path2):
    align_path = path2 + "/source-target.align"
    src_path = path1 + "/en_tok.txt"
    tgt_path = path1 + "/ch_tok.txt"
    save_path = path2 + "/token_source-target.align"

    src_tokens, tgt_tokens, ali_mapping = [], [], []

    with open(align_path, "r") as fa, open(src_path, 'r') as fs, open(tgt_path, 'r') as ft:
        src = fs.readlines()
        tgt = ft.readlines()
        ali = fa.readlines()

    length = len(src)

    for i in range(length):
        src_tokens.append(src[i].split())
        tgt_tokens.append(tgt[i].split())
        ali_mapping.append(ali[i].split())

    with open(save_path, "w") as f:
        for i in range(length):
            res = ""
            for k in range(len(ali_mapping[i])):
                src_index, tgt_index = ali_mapping[i][k].split('-')
                res += src_tokens[i][int(src_index)] + "-" + tgt_tokens[i][int(tgt_index)] + "\t\t"
            res += "\n"
        
            f.write(res)


def recover_backward(path1, path2):
    align_path = path2 + "/target-source.align"
    src_path = path1 + "/en_tok.txt"
    tgt_path = path1 + "/ch_tok.txt"
    save_path = path2 + "/token_target-source.align"

    src_tokens, tgt_tokens, ali_mapping = [], [], []

    with open(align_path, "r") as fa, open(src_path, 'r') as fs, open(tgt_path, 'r') as ft:
        src = fs.readlines()
        tgt = ft.readlines()
        ali = fa.readlines()

    length = len(src)

    for i in range(length):
        src_tokens.append(src[i].split())
        tgt_tokens.append(tgt[i].split())
        ali_mapping.append(ali[i].split())

    with open(save_path, "w") as f:
        for i in range(length):
            res = ""
            for k in range(len(ali_mapping[i])):
                src_index, tgt_index = ali_mapping[i][k].split('-')
                res += tgt_tokens[i][int(tgt_index)] + "-" + src_tokens[i][int(src_index)] + "\t\t"
            res += "\n"
        
            f.write(res)


def main(path1=r"/data1/wbxu/test_data", path2=r"/data1/wbxu/fast_align_res"):
    recover_forward(path1, path2)
    recover_backward(path1, path2)


main()