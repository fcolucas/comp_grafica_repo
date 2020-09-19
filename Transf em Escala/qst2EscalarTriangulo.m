function retval = qst2EscalarTriangulo()
	
	function pontosTransformados = transfEscalar(pontos, matriz)
    	pontosTransformados = pontos * matriz
	endfunction
  
  pontos = [0 0; 1 0; 0.5 2]
  matriz = [2 0; 0 2]
  
	pontos(length(pontos) + 1, :) = [pontos(1, 1) pontos(1, 2)]
	pontosTransformados = transfEscalar(pontos, matriz)
	plot(pontos(:, 1), pontos(:, 2), '-r*', 
		pontosTransformados(:, 1), pontosTransformados(:, 2), '-b*'
    )
   legend("original", "transformado") 
endfunction