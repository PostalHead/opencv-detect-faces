import argparse
import os
import cv2

DEFAULT_FOLDER_PATH = './img/'


def img_detect_faces(img_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not read image {img_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    return faces


def img_save_faces_rects(img_path, faces, img_out_path):
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not read image {img_path}")
        return

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(img_out_path, image)


def collect_img_paths_from_folder(folder_path):
    img_paths = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img_paths.append(img_path)

    return img_paths


def main():
    parser = argparse.ArgumentParser(description='Detect faces in images.')
    parser.add_argument('--image', type=str, help='Path to a single image file.')

    args = parser.parse_args()

    img_paths = []

    if args.image:
        if not os.path.isfile(args.image):
            print(f"Error: The file '{args.image}' does not exist.")
            return

        img_paths.append(args.image)
    else:
        if not os.path.isdir(DEFAULT_FOLDER_PATH):
            print(f"Error: The default folder path '{DEFAULT_FOLDER_PATH}' does not exist.")
            return

        img_paths = collect_img_paths_from_folder(DEFAULT_FOLDER_PATH)

    for img_path in img_paths:
        directory = os.path.dirname(img_path)
        directory = os.path.join(directory, 'out')
        os.makedirs(directory, exist_ok=True)

        faces = img_detect_faces(img_path)

        print(f"{img_path}:")
        for i, (x, y, w, h) in enumerate(faces):
            print(f"\t{i}: (x={x}, y={y}, w={w}, h={h})")

        img_out_path = os.path.join(directory, os.path.basename(img_path))
        img_save_faces_rects(img_path, faces, img_out_path)


if __name__ == '__main__':
    main()
