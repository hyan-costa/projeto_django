$(document).ready(function () {
    $('#table_id').DataTable();
});
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
            console.log(data['nome'])
            if(data['nome']){
                $('#cpf').addClass('is-invalid')
                let div = document.getElementById('cpfFeedback')
                $('#validacaoCpf').replaceWith("<div id=\"cpfFeedback\" class=\"invalid-feedback\">Usuário "+data['nome']+" já existe!</div>")


            }
            else {
                $('#cpf').removeClass('is-invalid')
                $('#cpfFeedback').value.remove()
            }

        }
    )
})