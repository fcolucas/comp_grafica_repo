function [vertParalelepipedo, facesParalelepipedo] = calculaVertParalelepipedo()
  %B - PARALELEPIPEDO
  p2 = [0 0 0];       % ponto inicial
  lx = 2;				      % lado em X
  ly = 4;             % lado em Y
  lz = 3;  			      % lado em Z

  %montando os pontos do paralelepipedo
  vertParalelepipedoOriginal = [ 	p2(1)      p2(2)      p2(3)     1;
                                  p2(1)      p2(2)+ly   p2(3)     1;
                                  p2(1)+lx   p2(2)+ly   p2(3)     1;
                                  p2(1)+lx   p2(2)      p2(3)     1;
                                  p2(1)      p2(2)      p2(3)+lz  1;
                                  p2(1)      p2(2)+ly   p2(3)+lz  1;
                                  p2(1)+lx   p2(2)+ly   p2(3)+lz  1;
                                  p2(1)+lx   p2(2)      p2(3)+lz  1;]';
            
  %Matriz de transformação
  mtPa = [  1  0  0   4 ;
            0  1  0  -4 ;
            0  0  1  -3 ];

  vertParalelepipedo = mtPa*vertParalelepipedoOriginal;
  facesParalelepipedo = [1 2 3 4; 2 6 7 3; 4 3 7 8; 1 5 8 4; 1 2 6 5; 5 6 7 8];
  
  patch('Faces',facesParalelepipedo,'Vertices',vertParalelepipedo','FaceColor','b');
  
  %PLOTA OS DETALHES
  xlabel ("x");					            % configura o nome da vetor X
  ylabel ("y");					            % configura o nome da vetor Y
  zlabel ("z");					            % configura o nome da vetor Z
  grid();							              % inicia a plotagem com as linhas de grade
  view (15, 30);				            % determina o angulo inicial de visão da plotagem
  print -djpg q1paralelepipedo.jpg;	% salva o  como jpg
  hold off; 
endfunction