class MultipleElementsHandler:
    def __init__(self, index, element):
        self.index = index
        self.element = element


def sort_list_multiple_elements_handlers(
    multiple_elements_handler_list: list[MultipleElementsHandler],
) -> list[MultipleElementsHandler]:
    return sorted(multiple_elements_handler_list, key=lambda k: k.index)
