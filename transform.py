import argparse

def transform(src, des):

    # read src
    ret = '"'
    with open(src) as fin:
        content = fin.readline()
        while content:
            # replace newline character
            content = content.replace('\n', '\\n')

            # replace quotation mark
            content = content.replace('"', '\\"')

            ret = ret + content
            content = fin.readline()
    ret = ret + '"'

    # write des
    # with open(des, 'w') as fout:
    #     fout.write(ret)
    print(ret)



if __name__=='__main__':
    p = argparse.ArgumentParser()
    p.add_argument('src', help='source file path')
    # p.add_argument('des', help='destination file path')
    args = p.parse_args()

    transform(args.src, args.des)
