def confidence_label(score):
    if score >= 7.5:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"
