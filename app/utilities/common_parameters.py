def convert_not_true_to_false(param_summary):
    if param_summary.lower() == 'true' or param_summary.lower() == True:
        return True
    else:
        return False
