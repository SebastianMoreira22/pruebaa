**1 - Indique los comandos para crear subir la versión del proyecto git a un repositorio remoto.**

Los comandos para hacer esto serían:
    
     git add . 
     git commit -m "mensaje" 
     git push origin "nombre de la rama"
    
**2 - ¿Cómo se puede utilizar el código de un proyecto git en un repositorio remoto (github) en un computador local?**

Para hacer esto, se debe clonar el repositorio remoto en el computador local, se utiliza el comando 
    
    git clone "url"
    
donde url es el link del repositorio remoto al cual ya se debe tener acceso.


**3 -  Si se implementa un código en python que crea un objeto de una clase abstracta, ¿Qué sucede al ejecutar dicho código?**

Al intentar ejecuta rdicho código, se produce un error, ya que no se puede crear un objeto de una clase abstracta, ya que esta no tiene implementado el método __init__.

A grandres rasgos, una clase abstracta no se puede instanciar directamente, por lo que se deben crear clases que hereden de ella y que no sean abstractas.

Al intentar ejecutar el código se produce el siguiente error:

    TypeError: Can't instantiate abstract class "nombre de la clase abstracta" with abstract methods "__init__"

**4 - ¿Qué significa que un método tenga el decorador @abstractmethod?**

esto se utiliza para indicar que en esa clase abstracta, lo siguiente que se va a definir es un método abstracto, el cual no tiene implementación, por lo que se debe implementar en las clases que hereden de esta.

**5 - Indique 3 eventos que pueden ejecutarse en una interfaz gráfica de usuario.**

Algunos de los eventos que se puede ejecutar en una GUI usando PyQt6 es el evento de presionar un botón, el evento de escribir en un cuadro de texto y el evento de seleccionar un elemento de una lista.

**6 - ¿Qué es el ciclo de eventos?**

El ciclo de eventos es un ciclo que se ejecuta constantemente en una GUI, el cual se encarga de detectar los eventos que se ejecutan en la interfaz gráfica y de ejecutar las funciones que se le asignaron a cada evento. Esto permite que la aplicación responda a las acciones del usuario en tiempo real.

**7 - Si desde la ventana principal de un programa se lanza un objeto de clase QDialog ¿Es posible ignorarlo y seguir utilizando la ventana principal?**

Sí es posible ignorar un QDialog y seguir utilizando la ventana principal. Puede hacerse creando el QDialog como no modal o ejecutándolo en su propio bucle de eventos, esto nos permite interactuar con la ventana principal mientras el QDialog está abierto.

**8 -  Mencione al menos 5 componentes gráficos de PyQt6**

QLabel utilizado para mostrar texto o imágenes.

QHBoxLayout utilizado para organizar los componentes gráficos en una ventana de forma horizontal.

QVBoxLayout utilizado para organizar los componentes gráficos en una ventana de forma vertical.

QPushButon utilizado para que el usuario pueda hacer click en un botón y ejecutar una acción.

QLineEdit utilizado para que el usuario pueda escribir texto.

**9 - Si se requiere de ingresar datos numéricos, qué alternativas existen de componentes en PyQt6**

QSpinBox, que permite ingresar un número y aumentar o disminuir su valor utilizando botones.

QDoubleSpinBox, que permite ingresar un número decimal y aumentar o disminuir su valor utilizando botones.

QSlider, que permite ingresar un número y aumentar o disminuir su valor utilizando un deslizador.


**10 -  ¿Cómo es posible utilizar una interfaz creada con Qt Designer en un código fuente en python con PyQt6?**

Se debe convertir el archivo .ui que se crea en Qt Designer a un archivo .py. 

Para hacerlo, utilizamos el siguiente comando en la terminal:

    pyuic6 "nombre del archivo .ui" -o "nombre del archivo .py"

Esto genera un archivo .py que contiene el código de la interfaz gráfica, el cual puede importarse en el código fuente en python y utilizarlo para crear la interfaz gráfica.




