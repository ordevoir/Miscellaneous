## Работа в терминале (Git Bash)
Download for [Windows](https://git-scm.com/download/win), [macOS](https://git-scm.com/download/mac), [Linux](https://git-scm.com/download/linux)
---

### Глобальные настройки

`git config --global user.email "wernadsky@gmail.com"`

`git config --global user.name "ordevoir"`

---

### Инициализация репозитория

Для инициализации репозитория, создаем папку (либо переходим в существующую) и вводим команду:

`git init`

При этом создается директория `.git`, в которой будет храниться история. Для того, чтобы "разгитить" директорию, достаточно удалить эту папку:

`rm -rf .git`         # recurcive-force remove

---

### Проверка статуса

Для проверки статуса репозитория используется команда

`git status`

---

### Добавление изменений

Для добавления изменений в репозиторий используется команда `git add`:

`git add file_name`   # для добавления изменений конкретного файла

`git add --all`       # для добавления изменений всех файлов

Добавление изменений препарирует файлы для фактического сохранения

---

### Сохранение изменений

для того, чтобы произвести фактическое сохранение добавленных изменений, необходимо вызвать команду `git commit`, при желании добавив сообщение:

`git commit -m "this is commit"`

---

### Журнал записей

Для того, чтобы посмотреть историю коммитов, необходимо ввести команду

`git log`

> [!Note]
> По умолчанию коммиты выводятся в обратном хронологическом порядке — последние коммиты оказываются первыми сверху

---

## Подключение удаленного репозитория (GitHub)

### Создание SSH-ключа
Прежде всего, для безопасной работы, следует сгенерировать SSH-ключ. Более подробная инструкция описана в [Яндекс Практикуме](https://practicum.yandex.ru/trainer/git-basics/lesson/42435683-0922-4231-bfb4-d7d32d61f50a/).

#### Проверка наличия SSH-ключа

`cd ~`

`ls -la .ssh/` # список созданных ключей

Если папка пустая или её нет, можно сгенерировать ключи. Если файлы ключей есть, но вы их не создавали, удалите их все.


#### Генерация SSH-ключа

`cd ~`

`ssh-keygen -t ed25519 -C "электронная почта, к которой привязан ваш аккаунт на GitHub"`

Если вы видите сообщение об ошибке, то, скорее всего, ваша система не поддерживает алгоритм шифрования `ed25519`. В этом случае используйте другой алгоритм

`ssh-keygen -t rsa -b 4096 -C "электронная почта, к которой привязан ваш аккаунт на GitHub"`

Далее можно указать место сохранения ключей, кодовую фразу (*passphrase*). Можно пропустить эти этапы просто нажав **Enter**. Тогда ключи будут созданы в директорории `./.ssh`, а кодовая фразау будет пустым. Если задать кодовую фразу, то придется вводить ее каждый раз при взаимодействии с удаленным репозиторием.

Теперь можно проверить, сгенерированны ли ключи:

`ls -a ~/.ssh`

На экране должны появиться два файла — один с расширением `.pub`, другой — без. Ключ в файле в `.pub` — публичный, им можно делиться с веб-сайтами или коллегами. Ключ в файле без расширения `.pub` — приватный.

-----------------

### Привязывание SSH-ключа к github
Скопируйте содержимое файла с публичным ключом в буфер обмена. В Windows можно использовать команду

`clip < ~/.ssh/id_ed25519.pub`

- Перейдите на GitHub и выберите пункт **Settings** в меню аккаунта(!). 
- В меню слева нажмите на пункт **SSH and GPG keys**. 
- В открывшейся вкладке выберите **New SSH key**.
- В поле **Title** напишите название ключа. Например, `Personal key`.
- В поле **Key type** должно быть **Authentication Key**.
- В поле **Key** скопируйте ваш ключ из буфера обмена.
- Нажмите на кнопку **Add SSH key**.
- Проверьте правильность ключа с помощью следующей команды:

`ssh -T git@github.com`

- Если это первый раз, когда вы используете Git, чтобы поделиться проектом на GitHub, появится похожее предупреждение:

`The authenticity of host 'github.com (140.82.121.4)' can't be established. ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU. This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?`

Это предупреждение сообщает, что вы никогда не соединялись с сервером GitHub. Поэтому Git не может гарантировать, что сервер является тем, за кого он себя выдаёт.

Для подтверждения подлинности сервер генерирует и публикует ключи SHA256. Вы можете проверить ключи GitHub по этой [ссылке](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints).

Если ключ в предупреждении совпадает с тем, что вы видите на сайте, значит, сервер является действительным. Введите `yes`, чтобы продолжить. Вы увидите приветствие на экране.

---------

### Связываем локальный и удалённый репозитории

Перейдите на страницу удалённого репозитория, выберите тип **SSH** и скопируйте URL.
Откройте консоль, перейдите в каталог локального репозитория и введите команду 

`git remote add origin git@github.com:ordevoir/bash_and_git.git`

Команде необходимо передать два параметра: имя удалённого репозитория и его URL. В качестве имени используйте слово `origin` - стандартный псевдоним, с помощью которого можно обращаться к главному удалённому репозиторию (обычно такой репозиторий один).

Для того, чтобы убедиться, что репозитории связаны, выведем список удаленных репозиториев:

`git remote -v`

Флаг `-v` — короткая форма флага `--verbose`. В выводе вы должны увидеть две строчки:

`origin  git@github.com:ordevoir/bash_and_git.git (fetch)`
`origin  git@github.com:ordevoir/bash_and_git.git (push)`

`git remote remove origin` - удаление репозитория из списка

-------------------------------------------

### Отправка изменения на удалённый репозиторий
После коммита можно загрузить содержимое локального репозитория на GitHub:

`git push -u origin master`   # первая отправка

В первый раз эту команду нужно вызвать с флагом `-u` и параметрами `origin` (имя удалённого репозитория) и `main` или `master` (название текущей ветки). Флаг `-u` свяжет локальную ветку с одноимённой удалённой. 

В дальнейшем, при работе с удалённым репозиторием, флаг `-u` можно опустить и писать просто 

`git push`                    # последующие отправки

-------------------------------------------

### Получение изменения из удалённого репозитория

`git pull origin master`

`git pull`

Следует иметь в виду, что `pull` производит также слияние, поэтому следует удостовериться, что в локальном репозитории проивзеден коммит.

---

`git branch` - показывает ветки (`*` текущая ветка)
`git branch new_br` - создает ветку `new_br`
`git checkout new_br` - переход на ветку `new_br`

`git push maxwell new_br` - заливка в ветку `new_br`

`git checkout -b new_br` - создает ветку `new_br` и сразу переходит на нее

для того чтобы влить ветку `new_br` в основную ветку `master`, нужно сначала перейти в ветку `master`:
`git checkout master` и затем выполнить слияние:
`git merge new_br`

`git branch -d new_br` - удалить ветку `new_br` (на самом github ветка при этом еще не удаляется)

---

## GitHub в VS Code

Если имеется аккаунт на GitHub, то все основные дейсвтия можно производить непосредственно в редакторе VS Code, причем использовать можно как графический интерфейс, так и терминал.

---

### Клонирование репозитория

Убедитесь, что в VS Code не открыта папка. Перейдите в представление проводника (**Ctrl+Shift+E**). Там будет кнопка **Clone**. После нажатия нужно будет указать ссылку на репозиторий.
