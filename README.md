# Jogo da Vida de Conway

O Jogo da Vida de Conway é um exemplo clássico de autômato celular que foi criado pelo matemático britânico John Horton Conway em 1970. O jogo é uma simulação de uma grade bidimensional de células vivas e mortas, que evoluem de acordo com regras simples baseadas no estado das células vizinhas. Embora as regras sejam muito simples, o jogo pode gerar padrões complexos e surpreendentes que se assemelham a estruturas encontradas na natureza.

## Como jogar

1. Comece criando uma grade bidimensional de células, que pode ser desenhada à mão ou usando um programa de computador. Cada célula pode estar viva ou morta.

2. Determine as regras de evolução do jogo. Cada célula na grade evolui de acordo com as seguintes regras:
   
   - Qualquer célula viva com menos de dois vizinhos vivos morre, como se estivesse causando solidão.
   - Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração.
   - Qualquer célula viva com mais de três vizinhos vivos morre, como se estivesse causando superpopulação.
   - Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva, como por reprodução.

3. Aplique as regras a todas as células na grade. Cada célula deve ser atualizada simultaneamente com base no estado das células vizinhas.

4. Repita o processo para gerar novas gerações de células.

## Aplicações

O Jogo da Vida de Conway tem aplicações em várias áreas, incluindo:

- Ciência da computação: o jogo é usado como um exemplo de algoritmo para simular a evolução de sistemas complexos.
- Biologia: o jogo pode ser usado para modelar o crescimento de populações e a interação entre organismos.
- Física: o jogo pode ser usado para estudar a dinâmica de sistemas em equilíbrio e a transição para estados caóticos.
- Economia: o jogo pode ser usado para modelar a dinâmica de mercados e a interação entre agentes econômicos.