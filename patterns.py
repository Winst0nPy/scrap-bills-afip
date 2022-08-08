import regex as re


def is_product_row(block):
    b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block

    def has_iva(text):
        ivas = ['27%', '21%', '10.5%', '5%', '2.5%']
        text = ' '.join(text[len(text)-7:])
        if any([iva in text for iva in ivas]):
            return True
        return False

    def is_last_index_float(text):
        try:
            var = float(text[-1].replace(',', '.'))
            return True
        except ValueError:
            return False

    if all([is_last_index_float(word) and has_iva(word) for word in text]):
        return True
    return False

