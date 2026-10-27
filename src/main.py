import os
from dotenv import load_dotenv
# Загружаем переменные из файла .env в систему
load_dotenv()
print('Hello from repository!')
def print_author():
	# Допишите здесь ваш код
	author = os.getenv("AUTHOR")
	print(f"Автор проекта: {author}")
print_author() 
