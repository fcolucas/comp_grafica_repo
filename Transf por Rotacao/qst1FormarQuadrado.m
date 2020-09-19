function res = qst1FormarQuadrado(pontos)
    function pontosTransformados = rotacao(pontos, angulo)
        M = [cos(angulo) sin(angulo); -sin(angulo) cos(angulo)]
        pontosTransformados = pontos * M    
    endfunction
    
    p3 = rotacao(pontos, pi/4)
    p4 = rotacao(pontos, pi/2)

    quadrado = [
    pontos(1, 1) pontos(1, 2);
    pontos(2, 1) pontos(2, 2);
    p3(2, 1) p3(2, 2);
    p4(2, 1) p4(2, 2)
    ]

    quadrado(length(quadrado)+1, :) = [quadrado(1, 1) quadrado(1, 2)]
    
    plot(
        quadrado(:, 1), quadrado(:, 2), '-r'
    )
endfunction
