import regex as re


def is_product_row(block):
    b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
    if len(text) < 7:
        return False
    IVA = ['27%', '21%', '10,5%', '5%', '2,5%']
    return any([iva == text[-2] for iva in IVA])


def is_cuit_in_text(text):
    pattern = re.compile(r'\d{11}')
    if any([words for words in text if pattern.search(words)]):
        return True


