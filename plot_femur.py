import numpy as np
import matplotlib.pyplot as plt


def load_obj(filename):

    vertices = []
    faces = []

    with open(filename) as f:
        for line in f:

            if line.startswith("v "):
                parts = line.split()
                x = float(parts[1])
                y = float(parts[2])
                vertices.append([x, y])

            elif line.startswith("f "):
                parts = line.split()[1:]

                face = []
                for p in parts:
                    v_index = int(p.split("/")[0]) - 1
                    face.append(v_index)

                faces.append(face)

    return np.array(vertices), faces


def extract_outer_face(vertices, faces):
    """Take the face with maximum vertices as the outline."""

    outer_face = max(faces, key=len)

    polygon = vertices[outer_face]

    return polygon


def plot_polygon(vertices, polygon):

    plt.figure(figsize=(6,6))

    # Vertices
    plt.scatter(vertices[:,0], vertices[:,1], s=10)

    # Outline
    poly_closed = np.vstack([polygon, polygon[0]])

    plt.plot(poly_closed[:,0], poly_closed[:,1], linewidth=2)

    plt.fill(polygon[:,0], polygon[:,1], alpha=0.2)

    plt.gca().set_aspect("equal")
    plt.title("Outer polygon from OBJ")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


def main():

    vertices, faces = load_obj("Femur_mm_0.obj")

    polygon = extract_outer_face(vertices, faces)

    print("vertices:", len(vertices))
    print("faces:", len(faces))
    print("outer polygon vertices:", len(polygon))

    plot_polygon(vertices, polygon)


if __name__ == "__main__":
    main()