Title: Прошивка RPi Compute Module
Slug: firmware-rpi

<!-- __#TODO: нужно дать ссылки на образы прошивок и нужный софт__ -->

## Введение

В качестве бортового компьютера на аппаратах MiddleAUV и MiddleUSV применяется
Raspberry Pi Compute Module. Этот модуль, внешне похожий на планку оперативной памяти,
имеет встроенную Flash-память, куда и будет записывать образ прошивки.

![](/media/firmware-rpi/overview.jpg)

Слева на картинке - отладочная плата. Справа - сам RPi Compute Module.

## Ссылки на образы и необходимое ПО

- [Образ для MiddleAUV](https://yadi.sk/d/TXavPwErRHBKcg) (`mur-auv-software`)
- [Образ для MiddleUSV](https://yadi.sk/d/XTlshffIK5B6fQ) (`usv-server`) <!-- надо сократить размер образа -->
- `usbboot` - [исходный код](https://github.com/raspberrypi/usbboot), [готовая сборка под GNU/Linux](https://yadi.sk/d/TZd48nW0k0CXfw)

## Инструкция

> В качестве альтернативы, можно обратиться к  [официальной инструкции Raspberry Pi](https://www.raspberrypi.org/documentation/hardware/computemodule/cm-emmc-flashing.md).
> Ниже описана инструкция для окружения GNU/Linux.

1.  Установить модуль в отладочную плату.

    ![](/media/firmware-rpi/module-installed.jpg)

2.  Можно использовать любой компьютер с GNU/Linux, где имеется нужный софт.

    Рассмотрим пример с Intel NUC. Нужно запустить Intel NUC,
    также можно и подключить его к локальной сети для управления по ssh:
    `ssh nuc@nuc.local`, логин - `nuc`, пароль - `nuc`.
    Альтернатива - подключить к NUC дисплей, клавиатуру и мышь, после чего
    использовать как десктоп.

3.  Подключить MicroUSB кабель к разъёму передачи данных (USB Slave),
    но не подключать питание.

    ![](/media/firmware-rpi/1-before-flashing.jpg)

4.  Проверим, какие дисковые разделы у нас имеются на данный момент:

        nuc@nuc:~/Raspberry/usbboot$ ls /dev/sd*
        /dev/sda  /dev/sda1  /dev/sda2  /dev/sda5

5.  Запускаем `rpiboot` от имени `root`:

        nuc@nuc:~/Raspberry/usbboot$ sudo ./rpiboot
        Waiting for BCM2835/6/7/2711...

6.  После появления надписи `Waiting for BCM2835/6/7/2711...` можно подавать питание:

    ![](/media/firmware-rpi/2-power.jpg)

7.  В нормальной ситуации должен быть следующий вывод в консоли:

        Waiting for BCM2835/6/7/2711...
        Sending bootcode.bin
        Successful read 4 bytes
        Waiting for BCM2835/6/7/2711...
        Second stage boot server
        File read: start.elf
        Second stage boot server done

8.  Проверим, что флеш-память модуля видна в `/etc/dev/`:

        nuc@nuc:~/Raspberry/usbboot$ ls /dev/sd*
        /dev/sda  /dev/sda1  /dev/sda2  /dev/sda5  /dev/sdb

    Видно, что появилось новое устройство `/dev/sdb`.

9.  Теперь можно загружать прошивку.

    Необходимо ввести команду `sudo dd if=образ.img of=/dev/sdX status=progres`,
    где `образ.img` - путь к образу прошивки, а `/dev/sdX` - устройство, которое
    ранее появилось после загрузки модуля.

    Пример:

        nuc@nuc:~/Raspberry/usbboot$ sudo dd if=mur_emmc.img of=/dev/sdb status=progress
        3277496832 bytes (3.3 GB, 3.1 GiB) copied, 1644 s, 2.0 MB/s
        6403209+0 records in
        6403209+0 records out
        3278443008 bytes (3.3 GB, 3.1 GiB) copied, 1646.21 s, 2.0 MB/s

    Это займёт некоторое время. В конце, если всё нормально, должны быть видны
    разделы `/dev/sdb1` и `/dev/sdb2`. На скриншоте приведена вся последовательность
    команд для успешной прошивки:

    ![](/media/firmware-rpi/screenshot.png)

10. После успешной прошивки не помешает провести тестовый запуск платы.

    Отключаем все USB-кабели. Втыкаем HDMI-кабель от монитора и USB-клавиатуру,
    а затем подключаем питание (без USB Slave, его не надо подключать).

    ![](/media/firmware-rpi/3-test-boot.jpg)

    Первый запуск скорее всего будет долгим (из-за расширения файловой системы),
    возможна перезагрузка - это нормально. Также является __нормальным__ сообщение
    об ошибке запуска сервиса `MUR service`.

    ![](/media/firmware-rpi/boot-log.jpg)

    Если удалось выполнить вход в систему (логин - `pi`, пароль - `raspberry`),
    то всё нормально.
