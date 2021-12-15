import yaml

def read_yaml(file):
    with open(file,encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        return yaml_data
#
# if __name__  == "__main__":
#     fil = r"E:\pythonProject0926\tests\setting\db.yaml"
#     print(read_yaml(fil))
#     print(read_yaml(fil)["host"])
#
