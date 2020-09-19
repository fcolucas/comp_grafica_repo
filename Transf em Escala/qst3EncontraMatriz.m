function retval = qst3EncontraMatriz()
	
	function pontosTransformados = transfEscalar(pontos, matriz)
    pontosTransformados = pontos * matriz
	endfunction
  
  function matrizTransf = encontraTrans(ptsAntes, ptsDepois)
    matrizTransf = ptsDepois'/ptsAntes'
  endfunction
  
  ptsAntes = [0 0; 0 1; 1 1; 1 0]
  ptsDepois = [0 0; 0 2.5; 1.5 2.5; 1.5 0]
  
  matriz = encontraTrans(ptsAntes, ptsDepois)
  pontos = ptsAntes
	pontos(length(pontos) + 1, :) = [pontos(1, 1) pontos(1, 2)]
	pontosTransformados = transfEscalar(pontos, matriz)
	plot(pontos(:, 1), pontos(:, 2), '-r*', 
		pontosTransformados(:, 1), pontosTransformados(:, 2), '-b*'
    )
   legend("original", "transformado") 
endfunction