from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = "email_user/activation.html"


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = "email_user/confirmation.html"


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "email_user/password_reset.html"


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = "email_user/password_changed_confirmation.html"


class UsernameResetEmail(email.UsernameResetEmail):
    template_name = "email_user/username_reset.html"


class UsernameChangedConfirmationEmail(email.UsernameChangedConfirmationEmail):
    template_name = "email_user/username_changed_confirmation.html"
