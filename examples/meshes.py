import nidity


print('meshes example')

nidity.reset()
m = nidity.meshes.add_mesh('MyMesh')
m.from_pydata(
    [
        # vertices
        # 0         1          2
        (1, 2, 3), (4, 5, 6), (7, 8, 9)
    ],
    [
        # edges
        (0, 1), (1, 2), (2, 0)
    ],
    [
        # faces
        (0, 1, 2),
    ]
)
print(m.vertices)
print(m.vertices.values())
print(m.vertices[0].co)
print(m.vertices[1].co)
print(m.vertices[2].co)
print(m.validate())
print(m.users)
