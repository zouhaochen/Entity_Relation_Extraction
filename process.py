import json
import pandas as pd
from config import *


def generate_rel():
    with open(SCHEMA_PATH, encoding='utf-8') as f:
        rel_list = []
        for line in f.readlines():

            print(line)
            exit()

            # json.load加载文本转化字典类型
            info = json.loads(line)

            # 取字典内关系predicate值
            # rel_list: id to relation
            rel_list.append(info['predicate'])

        # rel_list: relation to id
        rel_dict = {v: k for k, v in enumerate(rel_list)}
        df = pd.DataFrame(rel_dict.items())

        print(df)

        df.to_csv(REL_PATH, header=None, index=None)


if __name__ == '__main__':
    generate_rel()
