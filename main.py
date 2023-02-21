#Бэкап программ хранящих данные в файлах
import shutil
import os
import datetime

#Колличество дней хранения бэкапа
days = 7
#Папка, которую бэкапим
src = r"c:\yyr\src"
#Куда бэкапим
dst = r"c:\yyr\dst"
#Временная папка для копирования,
#т.к. файлы могут быть заняты работающей программой
tmp = r"c:\yyr\tmp"
#Лог файла
logF = r"\yyr\log.txt"

#функция логирования
def

#функция удаления страрых файлов
def del_old():
    ls = os.listdir(dst)
    for file in ls:
        if file.find("_") == -1:
            continue
        if (datetime.datetime.today() - datetime.datetime.strftime(file[0:file.find("_")], "%Y%m%d")).days >days:
            os.remove(f"{dst}\{file}")
    if __name__ == "__main__":
        try:
        #удалими временную папку, если её нет - игнорим
            shutil.rmtree(tmp, ignore_errors=True)
        #Получим текущую дату для имени файла
            today = datetime.datetime.today().strftime("%Y%m%d")
        #копируем всё во временную папку
            path = shutil.copytree(src, tmp)
        #Зададим имя файлу архива
            file_name = dst + f"\\{today}_srv-app1"
        #Создадим zip в папке назначения
            shutil.make_archive(file_name, "zip", path)
        #Удалим временную папку, её не может бысть, иначе пусть пишет лог
            shutil.rmtree(tmp)
        #Удалим файлы старше 7 дней
            del_old()
        #добавим в лог инфу об успешном бэкапе
            log(f" Succes backup\r\n From: {src}\r\n To: {file_name}.zip")
        except Exception as e:
        #что то пошло не так, запишем в лог текст ошибки
            log("ERORR \r\n"+ " " + str(e))