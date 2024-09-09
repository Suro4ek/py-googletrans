# from docx import Document
from googletrans import Translator
translator = Translator()
result = translator.translate('Этот метод позволит обновлять конкретную версию схемы потока, создавая новую версию на основе указанной.Важно отметить, что при обновлении сущности также нужно обновлять связанные сущности и создавать новые записи в таблице version_control. Это должно происходить в рамках одной транзакции для обеспечения целостности данных', dest='sah', src='ru')
print(result.text)