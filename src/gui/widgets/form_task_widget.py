import customtkinter as ctk
from gui.widgets.field_form_widget import FieldFormWidget

class FormTaskWidget(ctk.CTkFrame):
    STATUS_COLORS = {
        "to do": "#F44336",       # Rouge (Must Have)
        "in progress": "#FF9800", # Orange (Should Have)
        "done": "#4CAF50"         # Vert (Could Have)
    }

    def __init__(self, parent, submit_callback, **kwargs):
        """
        Widget de formulaire pour ajouter ou modifier une tâche.

        Args:
            parent: Le widget parent.
            submit_callback: Fonction callback appelée lors de la soumission du formulaire.
        """
        super().__init__(parent, **kwargs)
        self.submit_callback = submit_callback

        # Titre du formulaire
        ctk.CTkLabel(self, text="Ajouter une Tâche", font=("Arial", 16, "bold")).pack(pady=10)

        # Champ pour le titre
        self.field_title = FieldFormWidget(self, "Titre de la tâche :")
        self.field_title.pack(pady=8, fill="x")

        # Champ pour la description
        self.field_description = FieldFormWidget(self, "Description de la tâche :")
        self.field_description.pack(pady=8, fill="x")

        # Dropdown pour le statut
        ctk.CTkLabel(self, text="Statut de la tâche :", font=("Arial", 12)).pack(pady=(10, 0), anchor="w", padx=10)
        self.status_var = ctk.StringVar(value="to do")
        self.dropdown_status = ctk.CTkOptionMenu(self, variable=self.status_var, values=list(self.STATUS_COLORS.keys()))
        self.dropdown_status.pack(pady=8, fill="x", padx=10)

        # Bouton de soumission
        submit_button = ctk.CTkButton(self, text="Ajouter Tâche", command=self.on_submit,
                                      fg_color="#4CAF50", hover_color="#45a049")
        submit_button.pack(pady=20)

        # 📌 Légende des statuts (une seule ligne)
        legend_frame = ctk.CTkFrame(self, fg_color="transparent")
        legend_frame.pack(pady=10, fill="x", padx=10)

        ctk.CTkLabel(legend_frame, text="Légende :", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5)

        col = 1
        for status, color in self.STATUS_COLORS.items():
            label_frame = ctk.CTkFrame(legend_frame, fg_color=color, corner_radius=5)
            label_frame.grid(row=0, column=col, padx=5, pady=2)
            
            ctk.CTkLabel(label_frame, text=f" {status} ", font=("Arial", 12), text_color="white").pack(padx=5, pady=2)
            col += 1

    def on_submit(self):
        """Récupère les valeurs et appelle le callback."""
        title = self.field_title.get_value()
        description = self.field_description.get_value()
        status = self.status_var.get()

        if all([title, description, status]):
            self.submit_callback(title, description, status.lower())
            self.field_title.entry.delete(0, ctk.END)
            self.field_description.entry.delete(0, ctk.END)
            self.status_var.set("to do")
        else:
            print("Tous les champs doivent être remplis.")
