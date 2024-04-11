from shap_factory import ShapeFactory


if __name__ == "__main__":
    shape = ShapeFactory.get_shape('circle')

    if shape:
        shape.draw()
    else:
        print("Nothing to draw ...")
