

function add_carro(){

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
        console.log('teste')
    })

}