# Proyecto: Máquina Enigma
## *CC5301-1* Grupo 5

Este proyecto implementa una máquina Enigma, la cual fue una serie de distintos dispositivos de uso militar, desarrollada y utiilzado por el ejército Nazi durante la Segunda Guerra mundial. Su función consistía en encriptar y desencriptar mensajes, tomando como parámetro la configuración de sus componentes.

El encriptado consistía en la permutación de cada letra del alfabeto por otra, cuya pauta dependía de la configuración de cada máquina. Si bien existieron distintas versiones de la máquina Enigma con distintos componentes, todas seguían la estructura:
* Un cilindro de entrada - *Stator* o *Entrittswaize*: contiene el alfabeto, ordenado.
* Panel de conexiones- plugboard o *Steckerbrett*: permite conectar de 0 a 13 cables para intercambiar cualquier par de letras.
* Rotores - *Walzen*: la componente más relevante de la máquina, era un conjunto de I a VIII anillos más (posiblemente) uno beta y uno gamma, que mediante muescas rotaban y definían las reglas de sustitución alfabética. La rotación de los rotores seguía un mecanismo para añadir complejidad, que consistía en rotar la pieza dependiendo del carácter anterior (que a su vez depende del anterior y recursivamente del resto) y con ello cambiar la regla de sustitución del carácter actual, añadiendo acarreo en determinados momentos del proceso.
* Reflector: pieza que permite realizar la decodificación en la misma máquina, sin requerir de cambiar la configuración de la máquina.

Para utilizar esta implementación de la máquina Enigma, se debe:
1. Configurar la máquina.
    Por consola llamar `python configure_machine.py ROTORES POSICIONES PLUGBOARD REFLECTOR`, seleccionando:
    * Rotores: **4** valores entre: I, II, III, V, VI, VII y VIII, además de un Beta, pero que sólo puede estar en cuarta posición.
    * Posiciones: **4** valores entre 1 y 26 (inclusive).
    * Plugboard: De 0 a 13 pares de letras distintas, sin repetición.
    * Reflector: UKW-b o UKW-c.
    
    Por ejemplo, la configuración `python configure_machine.py III II I V 02 21 12 10 AU IR LM ZB QE HF VD UKW-c` significa:
    
    * Utilizar los rotores III, II, I y V, en ese orden.
    * El primer rotor (III) se posiciona inicialmente en 2, el segundo (II) en 21, el tercero (I) en 12 y el cuarto (V) en 10.
    * Conectar en el plugboard los pares (A,U), (I,R), (L,M), (Z,B), (Q,E), (H,F) y (V,D).
    * Utilizar el reflector UKB-c.
2. Encriptar el mensaje: