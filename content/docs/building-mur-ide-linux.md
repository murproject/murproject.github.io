# Сборка MUR IDE и Simulator в GNU/Linux

> TODO... На данный момент с поддержкой GNU/Linux имеется ряд проблем...

Предлагаю ориентироваться на сборочный конфиг snap (для MUR IDE и Simulator вместе) - [#TODO](github.com/.../snapcraft.yaml)

Он даст представление о том, какие пакеты нужно ставить (но в первую очередь это будет зависеть от используемого дистрибутива), с какими параметрами что собирать и т.д.

На что нужно отдельно обратить внимание:
- Версия Urho3D - 1.7.1
    - Скорее всего нужен будет патч: https://github.com/Zauzolkov/Urho3D/commit/832343bcb57fcdf487b4710123188d130f180235
- При сборке Urho3D важен параметр `URHO3D_PACKAGING=1`