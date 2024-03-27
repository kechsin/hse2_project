# Проект за второй курс
##Женя Лепихина
# Тональность комментариев YT-канала в зависимости от темы
Что я делаю: скачиваю комментарии YouTube-каналов по разным темам и смотрю, у каких из них самые позитивные или негативные комментарии.


Три этапа: всё скачать, определить тональность, проанализировать
## I. Всё скачать
Все тематические кластеры и каналы в каждом перечислены в channels.json и channels_to_json.py (более человеко-читаемый вид). Чтобы увидеть сами каналы, нужно вбивать id оттуда в ютьюб в формате "youtube.com/channel/{id}" (забыла предусмотреть нормальный список).
get_all_comments.py запускает функции из claster_get.py по каждому из кластеров. Список скачанных ID видео, скачанные комментарии, и заметки об ошибках кладутся в папку data. Затем comments_count.py считает, сколько всего комментариев получилось, и я руками перенесла это в comments_count.txt.

Чтобы запустить get_all_comments.py, вам нужно получить api-key тут: https://console.cloud.google.com/apis и положить его в файл secret.txt
## II. Определить тональность
get_sentiments.py отвечает за то, что мы пробегаемся по всем файлам типа comments_{cluster_name}.txt из data и смотрим все тональности. Они идут в файл sentiment_data.json.
## III. Проанализировать
Файл graphics.py строит несколько диаграмм и кладёт их в charts. (Самая информативная это global_chart.png). Ещё он делает файл normilized_final_data.csv (табличка с долей положительных/нейтральных/отрицательных комментов), и эта табличка ещё в table.png (добавлена руками).
Выводы находятся в conclusion.txt.


Описание остальных файлов:

ideas.txt - то, куда я набрасывала идеи в начале работы

libraries - список нужных библиотек

файлы, начинающиеся на test - не делают ничего в итоговой работе, просто в них я разбиралась, как работают соответствующие вещи.