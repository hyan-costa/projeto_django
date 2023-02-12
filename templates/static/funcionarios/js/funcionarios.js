
// $(document).ready(function () {
//     $('#table_id').DataTable();
// });
function apaga_funcionario(pk){
    $.post('/funcionarios/apaga_funcionario/',{
        pk_funcionario:pk
    },
        function (data){
            alert("Usuário Apagado")
            window.location.reload()
        })
}
function editar_funcionario(pk){
    $.post('/funcionarios/editar_funcionario/',{
        pk_funcionario:pk
    },
        function (data){
            alert("Usuário Editado")
            window.location.reload()
        })
}
$('#cpf').change( function (){
    let cpf = this.value
    csfr_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    $.post(
        '/funcionarios/ajax_validacao/',
        {
            cpf: cpf,
            csrfmiddlewaretoken: csfr_token
        },
        function (data){
            //console.log(data)
            if(data['nome']){
                $('#cpf').addClass('is-invalid')

                $('#validacaoCpf').replaceWith("<div id=\"cpfFeedback\" class=\"invalid-feedback\">Usuário " + data['nome'] + " já existe!</div>")
                $('#salvar').attr('disabled','')
                if($('#cpfFeedback')){
                    $('#cpfFeedback').text("Usuário " + data['nome'] + " já existe!")
                }
            }
            else if(data['erro']){

                if($('#cpfFeedback')){
                    $('#cpfFeedback').text(data['erro'])
                }

                $('#salvar').attr('disabled','')
                $('#cpf').addClass('is-invalid')


            }
            else {
                $('#salvar').removeAttr('disabled', '')
                $('#cpf').removeClass('is-invalid')
                $('#cpfFeedback').value()

            }

        }
    )
})
// $('#cpf').change( function () {
//     let cpf = this.value
//     if (cpf.length != 11) {
//         $('#cpf').addClass('is-invalid')
//         let div = document.getElementById('cpfFeedback')
//         $('#validacaoCpf').replaceWith("<div id=\"cpfFeedback\" class=\"invalid-feedback\">CPF Inválido!</div>")
//
//     } else {
//         $('#cpf').removeClass('is-invalid')
//         $('#cpfFeedback').value.remove()
//     }
// })




