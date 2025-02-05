from typing import Optional

from stegano import lsb

from sigmage.exceptions import ImageFormatException


def get_signature(input_image: str) -> Optional[str]:
    """Obtains the signature of the image at the supplied path.

    :param input_image: the input image path
    :return: the signature if the image is signed, else None
    """
    return lsb.reveal(input_image)


def set_signature(input_image: str, output_image: str, signature: str) -> None:
    """Signs the image at the input path with the supplied signature and saves it at the output image path.

    The output image must be of png format because lossless compression is required to sign an image.

    :param input_image: the input image path
    :param output_image: the output image path
    :param signature: the signature
    :return: None
    :raise ImageFormatException: if the output image format is not png
    """
    if not output_image or output_image.split('.')[-1] != 'png':
        raise ImageFormatException()

    lsb.hide(input_image, signature).save(output_image, 'png')
