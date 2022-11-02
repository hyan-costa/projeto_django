
//----------------------------------exibe o form add carro--------------------------------------------------------------
function add_carro(){
    console.log('asdfasdf')
    container = document.getElementById("form-carro")

    html = "<br><div class='row'> " +
                    "<div class='col-md'>" +
                        "<input type='text' placeholder='carro' class='form-control' name='carro'>" +
                    "</div>" +
                    " <div class='col-md'>  " +
                        "<input type='text' placeholder='Placa' class='form-control' name='placa'> " +
                    "</div>" +
                    " <div class='col-md'>  " +
                        "<input type='date' placeholder='ano' class='form-control' name='ano'> " +
                    "</div>" +
                "</div>"
    container.innerHTML += html


}
//------------------------------exibe um dos dois forms-----------------------------------------------------------------
function exibir_form(tipo){

    atualizar_cliente = document.getElementById('atualizar_cliente')
    adicionar_cliente = document.getElementById('adicionar_cliente')
    if(tipo == "1"){
        atualizar_cliente.style.display ="none"
        adicionar_cliente.style.display ="block"
    }
    else if(tipo == "2"){

        adicionar_cliente.style.display ="none"
        atualizar_cliente.style.display ="block"
    }
}

//----------------Retorna os dados do cliente via ajax fetch API para alterar os dados----------------------------------
function dados_cliente(){
    cliente_pk = document.getElementById('cliente_pk')
    csfr_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    data = new FormData()
    data.append('cliente_pk', cliente_pk.value)
    fetch("/clientes/atualiza_cliente/",{
        method:'POST',
        headers:{'X-CSRFToken':csfr_token},
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){

        document.getElementById('form_att_cliente').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']
        if(data == ""){
            document.getElementById('form_att_cliente').style.display = 'none'
        }
        div_carros = document.getElementById('carros')
        div_carros.innerHTML = ""
        for (i=0; i<data['carros'].length;i++){
            div_carros.innerHTML +=
                "<div class='row'>" +
                    "<form action='/clientes/update_carro/"+data['carros'][i]['id_carro']+"' method='POST'> " +
                        "<div class='row'>"+

                            "<div class='col-md'>" +
                                "<input class='form-control' type='text' name='carro' value='"+data['carros'][i]['fields']['carro'] +"'><br>"+
                            "</div>" +


                            "<div class='col-md'>" +
                                "<input class='form-control' type='text' name='placa' value='"+data['carros'][i]['fields']['placa'] +"'><br>"+
                            "</div>" +


                            "<div class='col-md'>" +
                                "<input class='form-control' type='text' name='ano' value='"+data['carros'][i]['fields']['ano'] +"'><br>"+
                            "</div>" +
                            "<div class='col-md'>" +
                                "<input class='btn btn-success' type='submit' value='Salvar'>"+
                            "</div>" +
                            "<div class='col-md'>" +
                                "<a class='btn btn-danger' href='/clientes/excluir_carro/"+ data['carros'][i]['id_carro']+"' >excluir</a>"+
                            "</div>"
                        "</div>"+
                    "</form>"+

                +"</div><br><br>"
        }
    })
}

// ---------------------------------Retorna dados via ajax fetch API para o formulario----------------------------------
function get_cep(cep){
    data = new FormData()
    data.append('cep_value', cep)
    csfr_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    fetch('/clientes/retorna_cep', {
        method:'POST',
        headers:{'X-CSRFToken':csfr_token},
        body: data
        }).then(function (response){
            return response.json()
    }).then(function (data){
        uf = document.getElementById('uf')
        localidade = document.getElementById('localidade')
        logradouro = document.getElementById('logradouro')

        uf.value = data['uf']
        localidade.value = data['localidade']
        logradouro.value = data['logradouro']
    })
}