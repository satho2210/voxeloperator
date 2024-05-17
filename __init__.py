
import fiftyone.operators as foo
import fiftyone.operators.types as types 
 

class AddNoteOperator(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="add_note_operator",
            label="Add Note",
            description="Add a note to the sample",
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
        inputs.str("note", label="Note", description="Enter your note")
        return types.Property(inputs)

    def execute(self, ctx):
        note = ctx.params["note"]
        sample = ctx.sample
        sample["notes"].append(note)
        sample.save()
        return {"note_added": note}

def register(p):
    """Always implement this method and register() each operator that your
    plugin defines.
    """
    p.register(AddNoteOperator)
 
 
