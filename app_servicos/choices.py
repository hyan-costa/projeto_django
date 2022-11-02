from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM","Trocar válvula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO ="BLC", "Balanceamento"
