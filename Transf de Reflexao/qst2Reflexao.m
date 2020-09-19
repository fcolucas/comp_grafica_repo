function retval = qst1ReflexaoQuadrado(pontos)
  function pontosTransformados = reflexao(pontos)
    M = [-1 0; 0 -1]
    pontosTransformados = pontos * M
  endfunction
  
  ponto1 = [1 -1]
  ponto2 = [1.5+ponto1(1, 1) ponto1(1, 2)]
  ponto3 = [1.5+ponto1(1, 1) -1.5+ponto1(1, 2)]
  ponto4 = [ponto1(1, 1) -1.5+ponto1(1, 2)]
 
  pontos = [ponto1(1, :); ponto2(1, :); ponto3(1, :); ponto4(1, :)]
  
  pontos(length(pontos)+1, :) = [pontos(1, 1) pontos(1, 2)]
  pontosTransformados = reflexao(pontos);
  plot( 
    pontos(:, 1), pontos(:, 2), '-b*', 
    pontosTransformados(:, 1), pontosTransformados(:, 2), '-r*'
  )
  legend("original", "transformado", "location", "southeast")
endfunction