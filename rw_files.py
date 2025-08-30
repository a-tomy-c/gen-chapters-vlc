import yaml


class RWFiles:
    def __init__(self):
        ...

    def create_yaml(self, path_file:str, data:dict) -> str:
        with open(path_file, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
        return f'file created {path_file}'
    
    def read_yaml(self, path_file:str) -> dict:
        with open(path_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def append_txt(self, path_file:str, line:str) -> str:
        with open(path_file, 'a', encoding='utf-8') as file:
            file.write(line)
        return f'add line {line}'
    


if __name__=="__main__":
    rw = RWFiles()
    res = ""