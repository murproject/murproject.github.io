Title: Протокол управления MiddleAUV и MiddleUSV
Slug: protocol-mur

[TOC]

Лучшим источником информации на эту тему остаются исходники.

# Общие принципы

Приложение (например, MUR IDE) подключается к аппарату (как правило IP-адрес 10.3.141.1) по протоколу WebSocket, порт 2090. При открытом подключении, аппарат будет периодически отсылать телеметрию.

Тип сообщения задаётся полем `type`, например: `{"type": "remote"}`

# Виды исходящих пакетов (управление аппаратом)

## `run` - запуск скрипта

```
type: 'run',
filename: "имя файла",
content: "закодированный в Base64 скрипт"
```

## `stop` - остановка скрипта

```
type: 'stop'
```

## `remote` - включить режим телеуправления

```
type: 'remote'
```

В режиме телеуправления также открываются видеопотоки.
Передача видео идёт другим способом.

## `stop_remote` - выключить режим телеуправления

```
type: 'stop_remote'
```

Иногда не срабатывает из-за того, что видеопотоки забивают WiFi-сеть.

## `thrust` - телеуправление: задать тягу движкам

Используется в режиме телеуправления, если нет регуляторов (полностью ручное упарвление)

```
type: 'thrust',
power: [
        firstUpwardMotor,
        firstForwardMotor,
        secondForwardMotor,
        secondUpwardMotor,
        0,
        0,
        0,
        0,
        0
    ]
```

## `remote_control` - телеуправление: задать оси и регуляторы

Полуавтоматическое управление с регуляторами по курсу и глубине

```
type: 'remote_control',
axes: [
        x,
        y,
        z,
        0
    ],
yaw: true,
depth: false
```

# Виды входящих пакетов (информация с аппарата)

## `telemetry` - телеметрия

```
vehicle_type:
            - он либо отсутствует (значит AUV)
            - либо USV для лодки

running     - выполняет скрипт
remote      - режим телеуправления
mission     - mission, это для лодки

yaw         - навигационно-пилотажный датчик
pitch
roll

battery
temperature

gps_satellites  - GPS, только на MiddleUSV
gps_lng
gps_lat
gps_alt
gps_speed
```

## `output` - вывод в консоли

```
stdout, stderr - соответствующий вывод из консоли.
```

# Видео с камер ([GStreamer](https://gstreamer.freedesktop.org))

Видео передается через GStreamer pipeline на тот же IP, который подключился по WebSocket. Видео кодируется в JPEG, заворачивается в RTP и передаётся по UDP, порты `5000` и `5001` на две камеры.

Чтобы открыть видеопоток в VLC (или для записи) можно сделать так: создать SDP-файл (например, `mur-camera0.sdp`) со следующим содержанием, который можно открыть в VLC:

```
c=IN IP4 127.0.0.1
m=video 5000 RTP/AVP 26
a=rtpmap:26 JPEG/90000
```

Если нужно в целях отладки симулировать видеопоток с аппарата без него (т.е. локально запустить аналогичный видеопоток, который можно посмотреть в MUR IDE), то можно воспользоваться такой командой:

```
gst-launch-1.0 -v filesrc location=video.mp4 ! decodebin ! jpegenc ! rtpjpegpay ! udpsink host=0.0.0.0 port=5000
```

Выдернуть один кадр в JPEG-файл:

```
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=1/1 ! rtpjpegdepay ! multifilesink location="img.jpg"
```