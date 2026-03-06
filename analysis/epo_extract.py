import json

input_file = "../data/input/cmeie/CMeIE_train.json"

matched_examples = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line.strip())
        spo_list = data.get("spo_list", [])

        pair_dict = {}
        found = False

        for spo in spo_list:
            subject = spo.get("subject")
            predicate = spo.get("predicate")
            obj = spo.get("object", {}).get("@value")

            key = (subject, obj)

            if key not in pair_dict:
                pair_dict[key] = set()

            pair_dict[key].add(predicate)

            if len(pair_dict[key]) > 1:
                found = True
                break

        if found:
            matched_examples.append(data)

print(f"共找到 {len(matched_examples)} 个符合条件的示例：\n")

for example in matched_examples:
    print(json.dumps(example, ensure_ascii=False, indent=2))
    print("-" * 80)