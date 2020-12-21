Title: Сборка MUR Simulator в Windows
Slug: building-mur-simulator

Можно считать это продолжением [сборки MUR IDE](./building-mur-ide). Предполагается, что уже имеется Qt, OpenCV и прочее что уже было ранее описано (не забываем аналогично прописать пути для CMake, где это необходимо).

## ZeroMQ

- Можно воспользоваться всё тем же vcpkg.
- А можно склонировать и собрать самостоятельно:
    - `git clone https://github.com/zeromq/libzmq`
    - `cd libzmq; mkdir build; cd build`
    - `cmake ..; cmake --build .`
    - Не забываем прописать путь для CMake: `set(ZeroMQ_DIR "D:/projects/libzmq/build")`

## Сборка Urho3D

- Urho3D придётся собирать самостоятельно.
- Рекомендуется ознакомится с [документацией по сборке Urho3D](https://urho3d.github.io/documentation/1.7.1/_building.html)
- `git clone https://github.com/urho3d/Urho3D`
- Далее нужно запустить CMake и сконфигурировать проект, можно воспользоваться cmake-gui. Параметры сборки:
    - `URHO3D_PACKAGING=1` (самое важное! требуется для загрузки ресурсов из файла)
    - `URHO3D_SAMPLES=0` (не собирать примеры)
    - `URHO3D_LUA=0` (поддержка скриптов в данном случае не нужна)
    - `URHO3D_ANGELSCRIPT=0`
- Конфигурируем проект, затем собираем.
    - Можно открыть и собрать проект в Visual Studio.
    - Или собрать прямо из консоли: `cd Urho3D/build; cmake --build .`
- Для сборки симулятора обязательно нужно будет прописать путь к Urho3D:
    - `set(URHO3D_HOME "D:/projects/Urho3D/build")`

## Сборка симулятора

- Клонируем проект [MUR Simulator](https://github.com/murproject/mur_simulator).
- Конфигурируем проект и собираем.
- Добавляем недостающие библиотеки Qt (QML здесь не нужен):
    - `windeployqt.exe "D:\projects\mur_ide\build\simulator.exe"`
- Также копируем недостающие библиотеки OpenCV и ZeroMQ.
- Файл ресурсов `simulator.pck` (можно найти в папке `resources`) __должен лежать рядом с собранным бинарником!__ Иначе ничего работать не будет.