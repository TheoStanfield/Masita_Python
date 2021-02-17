class Layer(object):
    def __on_event__(self, event) -> bool:
        pass

    def __on_update__(self) -> None:
        pass

    def __on_render__(self, display) -> None:
        pass

class LayerStack(object):
    def __init__(self):
        self.layer_stack:Layer = []

    def get(self):
        return self.layer_stack

    def push_layer(self, layer):
        self.layer_stack.append(layer)

    def push_overlay(self, overlay):
        self.layer_stack.insert(0, overlay)

    def pop_layer(self, layer):
        index = self.layer_stack.index(layer)
        self.layer_stack.remove(self.layer_stack[index])

    def pop_overlay(self, overlay):
        index = self.layer_stack.index(overlay)
        self.layer_stack.remove(self.layer_stack[index])

    def clean(self):
        for layer in self.layer_stack:
            del layer
