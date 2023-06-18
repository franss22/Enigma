Durante la Segunda Guerra Mundial los alemanes utilizaron la famosa Máquina Enigma, una máquina de encriptación basada principalmente en sustitución que gracias a la gran cantidad de combinaciones posibles que podía utilizar y que cambiaba cada día se consideraba poderosa. Y en efecto, demoró años de arduo trabajo para poder ser quebrada. Esta máquina se utilizaba por los militares para mandar mensajes importantes tales como avisos de ataques, buscando que no pudieran ser interceptados por los Aliados. La configuración de la máquina cambiaba cada día, los alemanes tenían un libro de códigos con la configuración diaria que iban siguiendo de forma coordinada para encriptar y desencriptarel mensaje correctamente. Esto añadía una gran complejidad a los Aliados para poder romper el sistema.

Este proyecto consiste en implementar una máquina Enigma. Para ello usted debe investigar sobre el funcionamiento de esta máquina, sus componentes, y el proceso de encriptación, para luego hacer una implementación coherente en el lenguaje que usted desee. La máquina debe funcionar a través de la ventanas de comandos, usted decide cómo diseñar el programa interactivo. 

Sin embargo la máquina debe cumplir con los siguientes requisitos:

- Debe programar su configuración a través de un mensaje del estilo "III II I V 02 21 12 10 AU IR LM ZB QE HF VD UKB-c". El cual significa que se utilizan los rotores III, II, I y V en dicho orden, las siguientes 4 instrucciones indican la posición en la cual se configura inicialmente cada rotor respectivamente, los siguientes pares de letras indican los intercambios del plugboard, y por último el texto final corresponde al reflector utilizado.
- Considere que pueden haber de 0 a 13 pares de letras para intercambio en el plugboard.
- Su máquina debe tener plugboard, 4 espacios para rotores y reflector.
- Los rotores disponibles para la utilización de su máquina deben ser: I, II, III, V, VI, VII, VIII y Beta. Se debe incluir la configuración original de las muescas para cada rotor. Sin embargo, para la muesca VIII le pedimos una configuración especial de muescas en la posiciones "V" y "A".
- Implemente correctamente la rotación de los rotores, incluyendo también la rotación en cascada cuando sea necesario.
- Los reflectores disponibles deben ser UKB-c y UKB-b.
- Se debe poder encriptar mensajes con su implementación.

Esta página le puede ser útil para ver la configuración de los rotores y de los reflectores solicitados:
Rotores y cableado de enigma

Tenga cuidado con copiar códigos desde Internet, puesto que son fácilmente identificables por el equipo docente. Además, tal como ya se mencionó, hay distintas variedades de máquinas Enigma y en este proyecto se les pide una máquina particular. Las soluciones de Internet no satisfacen todo lo expuesto anteriormente y por lo general son más básicas puesto que ignoran alguno de los detalles de funcionamiento. No se pueden utilizar librerías que contengan implementaciones para algunas de las partes de Enigma, ni tampoco una librería que contenga el funcionamiento completo de dicha máquina. Si bien GPT sirve para entender un poco mejor el funcionamiento de Enigma, tenga cuidado con su uso puesto que con respecto a la Máquina Enigma frecuentemente da respuestas incorrectas que no son fáciles de notar a menos que usted comprenda el funcionamiento.