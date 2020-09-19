function retval = qst1Cisalhamento()
  
  function pontosTransformados = cisalhamento(pontos, matriz)
    pontosTransformados = pontos * matriz;
  endfunction
  
  pontos = [1 1; 3 1; 2 3];
  M1 = [1 0.2; 0 1];
  M2 = [1 0; 0.3 1];
  M3 = [1 0.2; 0.3 1];
  
  pontos(length(pontos)+1, :) = [pontos(1, 1) pontos(1, 2)];
  
  cis1 = cisalhamento(pontos, M1);
  cis2 = cisalhamento(pontos, M2);
  cis3 = cisalhamento(pontos, M3);
  
  subplot(1,3,1), plot(pontos(:, 1), pontos(:, 2), '-r',
       cis1(:, 1), cis1(:, 2), '-b'), legend("original", "cisalhamento em M1");
  subplot(1,3,2), plot(pontos(:, 1), pontos(:, 2), '-r',
       cis2(:, 1), cis2(:, 2), '-b'), legend("original", "cisalhamento em M2");
  subplot(1,3,3), plot(pontos(:, 1), pontos(:, 2), '-r',
       cis3(:, 1), cis3(:, 2), '-b'), legend("original", "cisalhamento em M3");
  
endfunction
