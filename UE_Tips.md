# Viewport Navigation

`F` – фокус на выделенный объект

`Q, W, E, R` – select, translate, rotate, scale

**Ctrl + `** – переключение между local и world системами координат



`Alt + Translate` / `Rotate` – клонирование объекта

`Alt + 1` / `2` / `3` – переключение между режимами отображения

`[` / `]` – изменение Grid Size

`Shift + [` / `]` – изменение угла поворота при вращении объекта


## Perspective

`RBM` – вращение камеры вокруг своей оси

`Alt + LBM` – вращение вокруг центра сцены, или вокруг объекта, на котором было произведено фокусирование

`Mouse Wheel` – zoom

## Projection

`RBM` – сдвиг по сцене




# Draft

открыть cmd в режиме игры можно клавишей ~

отображение fps:
    cmd => stat fps


увеличение fps:
Edit => Project Settings
    Rendering
        отключаем:
        Dynamic Global Illumination Method: None
        Reflection Method:                  None
        Shadow Map Method:                  Shadow Maps

исправление запекания теней после перемещения объектов:
Build: Build Lightning Only
