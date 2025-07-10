# CSV Анализатор

Простой CLI-инструмент для фильтрации и агрегации данных из CSV-файлов. Поддерживает работу с любыми колонками, использует только стандартную библиотеку (кроме `tabulate` для вывода).

---

## Возможности

- Фильтрация с операторами: `>`, `<`, `=`
- Агрегация по числовым колонкам: `avg`, `min`, `max`
- Чтение любых CSV-файлов (без жёсткой привязки к колонкам)
- Удобный вывод в виде таблицы (через `tabulate`)
- Проверка кода через `flake8`
- Покрытие тестами на `pytest`

---  

```  python
python main.py --file product.csv --where "price>100" --aggregate "price=avg"
```
<img width="111" height="99" alt="Снимок экрана 2025-07-10 190231" src="https://github.com/user-attachments/assets/a32400e8-6908-4dd9-befb-00afb5398e11" />

```  python
python main.py --file product.csv --where "price>100"
```
<img width="520" height="189" alt="Снимок экрана 2025-07-10 190633" src="https://github.com/user-attachments/assets/28abfc77-9c4b-4634-8d6c-eea2e8ccd288" />
