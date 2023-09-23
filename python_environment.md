## Сreate environments with **conda**

В общем случае задача заключается в построении модели, способной классифицировать образцы ирисов на три класса, по заданным четырем признакам. Но для начала мы упростим задачу. Модель должна будет производить бинарную классификацию: разбивать образцы всего на два класса - "virginica" и "not verginica". Первый класс будем называть <span style="color: green"> "положительным"</span> $\oplus$, а второй - <span style="color: orange">"отрицательным" </span> $\ominus$. Создадим для этого новый массив меток, который будет содержать значения `1` для образцов положительного класса, т.е. для ирисов вида virginica и `-1` для образцов отрицательного класса, т.е. для остальных ирисов.

[Подробная инструкция](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)

`conda update conda` - желательно обновить conda перед созданием окружения

Для чистой установки c заданной версией python (вместо `--name` можно писать `-n`):

`conda create --name envname python=x.x`

Клонирование доругого окружения:

`conda create -n envname --clone someenv`

Создание окружения с заданными пакетами:

`conda create -n envname scipy numpy matplotlib jupyter`

Создание окружения с заданной версией интерр

Создание окружения с заданной версией интерпретатора и пакетами anaconda

`conda create -n envname python=x.x anaconda`
(with anaconda's packages)

`conda activate envname` - активация окружения envname

`conda deactivate` - деактивация окружения

Установка пакета в заданное окружение:

`conda install -n envname package`

Полное удаление окружения envname:

`conda remove -n envname --all`

Вывести список окружений:

`conda info --envs`


### Для возможности аквтивации в powershell:

`conda init powershell`

возможно, придется прописать еще и это в режиме администратора:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`

перезапустить powershell

---

## Сreate environments with **virtualenv**

`pip inatall virtualenv`

Create a new virtual environment by choosing a Python interpreter and making a `.\venv` directory to hold it:

`virtualenv --system-site-packages -p python3 ./venv`

Activate the virtual environment:

`.\venv\Scripts\activate`

Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:

`pip install --upgrade pip`
`pip list`  # show packages installed within the virtual environment

And to exit virtualenv later:

`deactivate`  # don't exit until you're done using TensorFlow
