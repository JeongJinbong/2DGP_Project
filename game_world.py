objects = []

def add_object(o):
    objects.append(o)

def update():
    for o in objects:
        o.update()

def render():
    for o in objects:
        o.draw()

def remove_object(o):
    for o in objects:
        o.remove()
        return
    raise ValueError('존재하지 않는 객체를 지울 수 없음')