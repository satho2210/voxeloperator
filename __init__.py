import fiftyone.operators as foo
import fiftyone.operators.types as types

class AddNoteOperator(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="add_note_operator",
            label="Add Note",
            description="Eine Notiz zum Sample hinzufügen",
            dynamic=False,
            execute_as_generator=False,
            unlisted=False,
            on_startup=False,
            on_dataset_open=False,
            allow_immediate_execution=True,
            allow_delegated_execution=False,
            default_choice_to_delegated=False,
            resolve_execution_options_on_change=None,
        )

    def resolve_input(self, ctx):
        inputs = types.Object()
        inputs.str("note", label="Notiz", description="Geben Sie Ihre Notiz ein")
        return types.Property(inputs)

    def execute(self, ctx):
        import logging
        logging.basicConfig(level=logging.DEBUG)
        
        note = ctx.params.get("note")
        if note is None:
            raise ValueError("Keine Notiz angegeben")

        # Debugging: Logge die Kontextattribute, um das Sample zu finden
        logging.debug(f"Kontextattribute: {dir(ctx)}")
        
        # Annahme, dass das Sample in ctx.view ist, falls ctx.sample nicht verfügbar ist
        if hasattr(ctx, 'sample'):
            sample = ctx.sample
        elif hasattr(ctx, 'view'):
            sample = ctx.view.first()  # Annahme, dass Sie das erste Sample in der Ansicht möchten
        else:
            raise AttributeError("Kein Sample oder View im Kontext gefunden")

        if 'notes' not in sample:
            sample['notes'] = []
        sample['notes'].append(note)
        sample.save()
        return {"note_added": note}

def register(p):
    """Implementieren Sie immer diese Methode und registrieren Sie jeden Operator,
    den Ihr Plugin definiert.
    """
    p.register(AddNoteOperator)
