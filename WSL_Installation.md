# Предварительные действия

Первым делом необходимо включить дополнительные функции Windows. Для этого нажмите **Win**, и найдите `Turn Windows features on or off`. Включите следующие функции:

- Windows Subsystem for Linux
- Virtual Machine Platform

Дождитесь установки. Может потребоваться перезагрузка.

# Установка WSL

Для установки Windows Subsystem for Linux откройте PowerShell от имени администратора и выполните

```bash
wsl --update --web-download
wsl --install
```

По умолчанию будет установлен Ubuntu. Можно также выбрать другой дистрибутив, например:

```bash
wsl --install -d Ubuntu-22.04
```
Для того, чтобы проверить, какой дистрибутив установлен, можно воспользоваться коммандами:
```bash
lsb_release -a
```
или
```bash
cat /etc/os-release
```



Список доступных дистрибутивов можно посмотреть так:


```bash
wsl --list --online
```

> При возникновении ошибки Error 0x80370102 один из вариантов исправить – переключиться на WSL1:
>
> `wsl --set-default-version 1`

# [VS Code в WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

Установить [VS Code](https://code.visualstudio.com/download) нужно на Windows (не на систему WSL). 

Необходимо установить расширение [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

Обновите Linux:

```bash
sudo apt-get update
```

Чтобы добавить wget (для получения контента с веб-серверов) и ca-сертификаты (чтобы приложения на основе SSL могли проверять подлинность SSL-соединений), выполните:

```bash
sudo apt-get install wget ca-certificates
```

Для того, чтобы запустить VS Code из определенной директории Linux, нужно перейти в bash к соответствующей директории и выполнить

```bash
code .
```

Также можно просто открыть VS Code и переключиться на окружение WSL нажав значок Open Romote Window (в нижнем левом углу окна редактора) и выбрав Connect to WSL.
