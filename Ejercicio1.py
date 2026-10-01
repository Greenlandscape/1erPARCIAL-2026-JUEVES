'''
## Ejercicio 1: La Serie de Potencias de Homero

Generar una lista por compresión que contenga la cantidad de donas que Homero consume en el infierno. Por cada dona que Homero consume apareceran más donas al ritmo de raíz de dos donas ($\displaystyle \sqrt{2}$) en su suplicio hasta que reviente.  

Ejemplo: <code>{ 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }</code>

'''

import math

N = 10
# resolvemos haciendo tuplas dentro de una lista ya que se pide lista por comprension.

[(dona, math.sqrt(2) ** (dona - 1)) for dona in range(1,N)]

# range a partir de una dona
# (dona - 1) para que empiece por 1