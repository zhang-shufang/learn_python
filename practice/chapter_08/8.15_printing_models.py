import printing_functions as printer

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printer.print_models(unprinted_designs, completed_models)
printer.show_completed_models(completed_models)