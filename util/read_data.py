import yaml


def get_data():
    # t = open("../config/data.yml", encoding="utf8")
    t = open("./config/data.yml", encoding="utf8")
    load = yaml.safe_load(t)
    print(load)
    print(load["hero"])
    print(load["hero_names"])
    print(load["heroes"])
    print(load["hero_name_list"])
    print(load["hero_list"])
    return load


if __name__ == '__main__':
    get_data()
