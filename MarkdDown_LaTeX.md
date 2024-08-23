# Раскрывающиеся области

Вот пример простейшей раскрывающейся (открытой) области:
<details open>

  ```html
  <details open>
    Content
  </details>
  ```
</details>

Пример раскрывающейся закрытой области с произвольным названием:
<details>
  <summary>Closed Collapsible Section</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

  ### Some Javascript
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>

# Символы 

$ \in $ – `\in`<br>
$ \owns $ – `\owns`<br>
$ \sim $ – `\sim` <br>
$ \rightarrow $ – `\to`, `\rightarrow` <br>
$ \leftarrow $ – `\leftarrow` <br>
$ \downarrow $ – `\downarrow` <br>
$ \uparrow $ – `\uparrow` <br>

# Варианты стилизации буквы


$ H $ <br>
$ \mathit H $ – `\mathit H` <br>
$ \mathrm H $ – `\mathrm H` <br>
$ \mathbf H $ – `\mathbf H` <br>
$ \mathbb H $ – `\mathbb H` <br>
$ \mathcal H $ – `\mathcal H` <br>
$ \mathfrak H $ – `\mathfrak H` <br>
$ \mathsf H $ – `\mathsf H` <br>
$ \mathtt H $ – `\mathtt H` <br>

$ h $ <br>
$ \mathrm h $ – `\mathrm h` <br>
$ \mathbf h $ – `\mathbf h` <br>
$ \mathfrak h $ – `\mathfrak h` <br>
$ \mathsf h $ – `\mathsf h` <br>
$ \mathtt h $ – `\mathtt h` <br>


# Добавление промежутков

$A B$ <br>
$A \, B$ – `A \, B` <br>
$A ~ B$ – `A ~ B` <br>
$A \quad B$ – `A \quad B` <br>
$A \qquad B$ – `A \qquad B` <br>
$A \hspace{0.5em} B$ – `A \hspace{0.5em} B` <br>

# Многоточия

$x_1 + \ldots + x_n$ – `\ldots`

$x_1 + \cdots + x_n$ – `\dots`, `\cdots`
 
$x_1 + \ddots + x_n$ – `\ddots`

$x_1 \quad \vdots \quad x_n$ – `\vdots`

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix}
$$

# Разное

Cкобки, высота которых соответствует содержимому:

$$
\left(  \sum_{i=1}^n x_i \right)
$$

$$
\left[  \sum_{i=1}^n x_i \right]
$$

$$
\left\{  \sum_{i=1}^n x_i \right\}
$$

$$
\left\lfloor \frac{x}{y} \right\rfloor\
$$

$$
\left\lceil \frac{x}{y} \right\rceil\
$$