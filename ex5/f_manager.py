import os


class FileManager:
    def __init__(self):
        self.path: str = "C:/Users/i.bondarenko/Desktop/task_practice/ex5/example"
        self.list_files: list = []

    def find_files(self):
        for f in os.listdir(self.path):
            full_path: str = self.path + str(f)
            self.list_files.append(full_path)
        return self.list_files

    def get_basename(self, path: str):
        filename = os.path.basename(path)
        return filename

    async def read_file(self, file: str):
        async with open(
            file=file,
            mode="r",
            encoding="utf-8",
        ) as file:
            pass


fm = FileManager()
