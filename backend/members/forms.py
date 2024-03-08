from django import forms
from .models import *


class TrainerForm(forms.ModelForm):
    class Meta:
        # indica que este formulario está asocioado al modelo Trainer
        model = Trainer
        # inida que todos los campos del modelo Trainer deben estar disponibles en el formulario
        fields = "__all__"

    def clean(self):
      
        cleaned_data = super().clean()
        errors = {}

        for field in [
            "birth",
            "dni",
            "address1",
            "phone",
        ]:
            if not cleaned_data.get(field):
                errors[f"{field}Empty"] = f"Debe introducir un {field}."
        if "email" in cleaned_data:
            email = cleaned_data["email"]
            try:
                forms.EmailField().clean(email)
            except forms.ValidationError:
                errors["wrongEmail"] = "Debe introducir un correo electrónico valido."
        if errors:
            cleaned_data["errors"] = errors
        return cleaned_data
