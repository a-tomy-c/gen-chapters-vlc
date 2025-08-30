# gen-chapters-vlc

video player usando vlc con python

- python 3.13.5
- python-vlc


## Notas

- agregado de player vlc
- creacion del ui


## fix

**player**

- ff y rw se cambio de 10 a 20 (antes:100), el valor del slide solo es de 1000
- se agrego metodos para obtener info timestamp, actual y restante y duracion
- cambie set_position por set_time para anterior y siguiente frame
- se agrego un if para verificar el estado, al estar en pause o detenido el timer se detiene
- al hacer la captura se retorna la ruta de la captura (para cargar como icono a la lista)
- se corrigio el metodo para adelantar o retrasar (es por tiempo ya por posicion)


**mk-chapter**

- se agrego dos listas uno para chapters y otro para star
- boton toggle para ver listas
- temporizador para cargar el icono del item luego de hacer la captura
- el texto del item usa `\n` (salto de linea) como separador entre el timestamp y los milisegundos
