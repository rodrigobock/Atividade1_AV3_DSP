$(function() {
    
    $.ajax({
        url: 'http://localhost:5000/listar_carros',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (Carro) {
        for (var i in Carro) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
              '<td>' + Carro[i].Modelo + '</td>' + 
              '<td>' + Carro[i].Marca + '</td>' + 
              '<td>' + Carro[i].QtdePortas + '</td>' + 
              '<td>' + Carro[i].Motor + '</td>' + 
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaCarros').append(lin);
        }
    }
});