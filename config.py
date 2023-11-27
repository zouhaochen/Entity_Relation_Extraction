import torch

# 关系表文件地址
REL_PATH = './data/output/rel.csv'

# 关系种类数量
REL_SIZE = 48

# 原始文件
SCHEMA_PATH = './data/input/duie/duie_schema.json'

TRAIN_JSON_PATH = './data/input/duie/duie_train.json'
TEST_JSON_PATH = './data/input/duie/duie_test.json'
DEV_JSON_PATH = './data/input/duie/duie_dev.json'


# SCHEMA_PATH = './data/input/cmeie/schema.json'

# TRAIN_JSON_PATH = './data/input/cmeie/train.json'
# TEST_JSON_PATH = './data/input/cmeie/CMeIE_test.json'
# DEV_JSON_PATH = './data/input/cmeie/CMeIE_dev.json'

BERT_MODEL_NAME = './hugging_face/bert-base-chinese'

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

BATCH_SIZE = 8
BERT_DIM = 768
LR = 1e-4
EPOCH = 50
MODEL_DIR = './data/output/'

# 0位置降权(后续需要调整)
CLS_WEIGHT_COEF = [0.3, 1.0]
SUB_WEIGHT_COEF = 3

SUB_HEAD_BAR = 0.5
SUB_TAIL_BAR = 0.5
OBJ_HEAD_BAR = 0.5
OBJ_TAIL_BAR = 0.5

EPS = 1e-10
