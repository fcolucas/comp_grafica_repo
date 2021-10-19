function [] = qst1Losango()
  % coordenadas dos pontos do quadrado
  % usamos R3 para calcular a translação por uma matriz
  p1 = [1, 1, 1];
  p2 = [2, 1, 1];
  p3 = [2, 2, 1];
  p4 = [1, 2, 1];
  
  quadrado = [p1; p2; p3; p4];
  Mr = [cos(pi/4) -sin(pi/4) 0; sin(pi/4) cos(pi/4) 0; 0 0 1]; %matriz de rotação a 45º
  Mt = [1 0 -1; 0 1 -1; 0 0 1]; %matriz de translação
  Mt2 = [1 0 1; 0 1 1; 0 0 1]; %matriz de translação (final)
  Me = [sqrt(2) 0 0; 0 2*sqrt(2) 0; 0 0 1]; %matriz de escalonamento
  
  quadT = (Mt * quadrado')'; %transladando o quadrado para origem (0,0)
  quadR = (Mr * quadrado')'; %rotacionando o objeto em 45º no sentido anti-horario
  quadE = (Me * quadR')'; %escalando os pontos das diagonais
  
  losango = (Mt2 * quadE')'; %transladando novo objeto para ponto inicial
  
  subplot(1, 2, 1), fill(quadrado(:, 1), quadrado(:, 2), 'r'), title("Antes"); 
  subplot(1, 2, 2), fill(losango(:, 1), losango(:, 2), 'r'), title("Depois");
  
endfunction
