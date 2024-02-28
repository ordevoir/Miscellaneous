import numpy as np
import matplotlib.pyplot as plt

def bgr2rgb(image):
    image_rgb = image.copy()
    for y in range(image_rgb.shape[0]):
        for x in range(image_rgb.shape[1]):
            image_rgb[y, x, 0], image_rgb[y, x, 2] = image_rgb[y, x, 2], image_rgb[y, x, 0]
    return image_rgb


def show_image(image: np.ndarray, title=None, size=8, 
                facecolor="gray", **options):
    plt.figure(figsize=(size, size), facecolor=facecolor)
    plt.axis("off")
    plt.title(title)
    plt.imshow(image, **options)
    plt.show()


def show_image_bgr(image: np.ndarray, title=None, size=8, **options):
    show_image(bgr2rgb(image), title, size, **options)

def show_images(images, titles=None, n_cols=2, size=4, facecolor="gray", **options):

    if titles is not None:
        assert len(titles) == len(images), "images count and titles count must be same"

    ratio = images[0].shape[0] / images[0].shape[1]     # height / width
    img_count = len(images)

    if img_count == 1:
        title = None if titles is None else titles[0]
        show_image(images[0], title, size, facecolor, **options)
        return

    n_cols = min(img_count, n_cols)
    n_rows = (img_count - 1) // n_cols + 1
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, 
                             figsize=(size*n_cols, size*n_rows*ratio))
    fig.set_facecolor(facecolor)
    
    if n_rows == 1:
        for i, img in enumerate(images):
            axes[i].axis("off")
            axes[i].imshow(img, **options)
            if titles:
                axes[i].set_title(titles[i])

    else:
        for i, img in enumerate(images):
            row, col = divmod(i, n_cols)

            axes[row, col].axis("off")
            axes[row, col].imshow(img, **options)
            if titles:
                axes[row, col].set_title(titles[i])
        
        while i < n_rows * n_cols:
            row, col = divmod(i, n_cols)
            axes[row, col].axis("off")
            i += 1

    plt.tight_layout()
    plt.show()

def show_images_bgr(images, titles=None, n_cols=2, size=4, facecolor="gray", **options):
    images_rgb = []
    for image in images:
        images_rgb.append(bgr2rgb(image))
    show_images(images_rgb, titles, n_cols, size, facecolor, **options)
