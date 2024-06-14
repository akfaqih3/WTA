from .models import *

models_dict = {
    'Stores':Store,
    'Brands':Brand,
    'Categories':Category,
    'Units':Unit,
    'Products':Product
}

def get_list_by_template_name(template_name)->models:

    if template_name in models_dict :
        return models_dict[template_name]
    else:
        return None
    