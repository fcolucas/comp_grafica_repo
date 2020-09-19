function [] = qst2Cubo()
  function pontosTransformados = cisalhamento(pontos, matriz)
    pontosTransformados = pontos * matriz;  
  endfunction
  
  cubo = [1 1 0;
          0 1 0;
          0 1 1;
          1 1 1;
          0 0 1;
          1 0 1;
          1 0 0;
          0 0 0];
  faces = [1 2 3 4;
           4 3 5 6;
           6 7 8 5;
           1 2 8 7;
           6 7 1 4;
           2 3 5 8];
   
   M1 = [1 0.4 0; 0 1 0; 0 0 1];
   M2 = [1 0 0; 0.4 1 0; 0 0 1];
   
   cis1 = cisalhamento(cubo, M1);
   cis2 = cisalhamento(cubo, M2);
   subplot(1,3,1), patch("Faces", faces, "Vertices", cubo, 'FaceColor', 'b'),
   title("Original")
   subplot(1,3,2), patch("Faces", faces, "Vertices", cis1, 'FaceColor', 'r'),
   title("Transformação em M1") 
   subplot(1,3,3), patch("Faces", faces, "Vertices", cis2, 'FaceColor', 'g'),
   title("Transformação em M2")
  
endfunction
