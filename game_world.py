objects = [[], []]
# layer 0 : Background Object
# layer 1 : Foreground Object

def add_object(o, depth=0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol

def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('존재하지 않는 객체를 지울 수 없음')
