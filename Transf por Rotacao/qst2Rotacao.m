function res = qst2RotacaoQuad(pontos)
    function pontosTransformados = rotacao(pontos, angulo)
        M = [cos(angulo) -sin(angulo); sin(angulo) cos(angulo)]
        pontosTransformados = pontos * M    
    endfunction
    
    pontos(length(pontos)+1, :) = [pontos(1, 1) pontos(1, 2)]
    O1 = rotacao(pontos, pi/4)
    O2 = rotacao(pontos, pi/2)
    O3 = rotacao(pontos, 3*pi/4)
    O4 = rotacao(pontos, pi)
    
    plot(
        pontos(:, 1), pontos(:, 2), '-r',
        O1(:, 1), O1(:, 2), '-b',
        O2(:, 1), O2(:, 2), '-k',
        O3(:, 1), O3(:, 2), '-y',
        O4(:, 1), O4(:, 2), '-g'
    )
endfunction
