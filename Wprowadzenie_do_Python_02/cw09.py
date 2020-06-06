from Wprowadzenie_do_Python_02.file_manager import FileManager


file_manager = FileManager('text.txt')

print(file_manager.read_file())
file_manager.update_file(" Pythonie.")
print(file_manager.read_file())
