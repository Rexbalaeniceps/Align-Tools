import os

def fast_align_preprocess(path1, path2):
    src_path = path1 + "/en_tok.txt"
    tgt_path = path1 + "/ch_tok.txt"
    res_path = path2 + "/result.txt"
    
    with open(src_path, "r") as src_file, open(tgt_path, "r") as tgt_file:
        src_sentences = src_file.readlines()
        tgt_sentences = tgt_file.readlines()
    
    with open(res_path, "w") as file:
        for src, tgt in zip(src_sentences, tgt_sentences):
            res = src[:-1] + " ||| " + tgt[:-1]
            file.write(res + "\n")


def use_fast_align(path):
    align = r"/data1/wbxu/fast_align/build/fast_align"
    atools = r"/data1/wbxu/fast_align/build/atools"
    res_path = path + "/result.txt"
    save_path1 = path + "/source-target.align"
    save_path2 = path + "/target-source.align"
    save_path3 = path + "/symmetrized.align"

    total_path_forward = align + " -i " + res_path + " -d -o -v > " + save_path1
    os.system(total_path_forward)

    total_path_reverse = align + " -i " + res_path + " -d -o -v -r > " + save_path2
    os.system(total_path_reverse)

    symmetrize_path = atools + " -i " + save_path1 + " -j " + save_path2 + " -c grow-diag-final-and > " + save_path3
    os.system(symmetrize_path)


def main(path1=r"/data1/wbxu/test_data", path2=r"/data1/wbxu/fast_align_res"):
    fast_align_preprocess(path1, path2)
    use_fast_align(path2)


main()