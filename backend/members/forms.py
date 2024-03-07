from django import forms


class SignupForm(forms.Form):
    # Comparacion de los campos y validación
    # Los campos se deben llamar igual a lo que pasemos por el request.POST
    email = forms.EmailField()
    password = forms.CharField(min_length=8)
    name = forms.CharField()
    surname = forms.CharField()

    # add_error es un método que nos prooporciona forms.Form
    # Los errores los almacena en errors
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("email"):
            self.add_error("email", "Debe proporcionar un correo electrónico válido.")
        if not cleaned_data.get("password"):
            self.add_error("password", "Debe proporcionar una contraseña.")
        elif len(cleaned_data["password"]) < 8:
            self.add_error(
                "password", "La contraseña debe tener al menos 8 caracteres."
            )
        if not cleaned_data.get("name"):
            self.add_error("name", "Debe proporcionar un nombre.")
        if not cleaned_data.get("surname"):
            self.add_error("surname", "Debe proporcionar un apellido.")
