from todos.constants.template_constants import BUTTON_LABELS

def add_template_constants(request):
    return {
        'BUTTON_LABELS': BUTTON_LABELS,
        'HOME': 'Home',
    }