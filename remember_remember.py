import cv2


def get_encrypted_message_from_image(image_path: str) -> str:
    """
        The function receives a path to an image and returns the message encrypted in it.
        Each column in the image has one pixel painted black.
        The pixel is colored by the line number that matches the numeric value of the character,
        and if you convert the position where the black pixels are from left to right,
        you get the encrypted message.
        :param image_path: The image contains an encrypted message.
        :return: The message encrypted in the image.
    """
    img = cv2.imread(image_path, 1)
    rows, cols, _ = img.shape
    encrypted_message = [chr(row) if all(img[row, col] == [1, 1, 1]) else ''
                         for col in range(cols) for row in range(rows)]
    return ''.join(encrypted_message)


if __name__ == '__main__':
    print(get_encrypted_message_from_image('code.png'))
