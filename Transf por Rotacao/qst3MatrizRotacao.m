% qst3MatrizRotacao: dado os pontos de um objeto e o ângulo de rotação, plota a 
% figura original e a rotação desse objeto no sentido horário
function retval = qst3MatrizRotacao(pontos, angulo)
  
  % rotacao2: dado os pontos de um objeto e o ângulo de rotação, retorma a 
  % rotação desses pontos no sentido horário
  function pontosTransformados = rotacao2(pontos, angulo)
    M = [cos(angulo) sin(angulo); -sin(angulo) cos(angulo)]
    pontosTransformados = M * pontos
  endfunction
  
  pontos(length(pontos) + 1, :) = [pontos(1, 1) pontos(1, 2)]
  pontosTransformados = (rotacao2(pontos', angulo))'
  plot(
    pontos(:, 1), pontos(:, 2), '-r',
    pontosTransformados(:, 1), pontosTransformados(:, 2), '-b'
  )
  legend("original", "rotação sentido horário")
endfunction
