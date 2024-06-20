import cv2 as cv2list


def load_known_faces():
    index = 0
    arr = []
    print("Start loop")
    while True:
        print("\n ***** Run again *****", index)
        cap = cv2list.VideoCapture(index)
        if not cap.read()[0]:
            print("Break from loop at:", index)
            break
        else:
            print("Continue in loop at:", index)
            arr.append(index)
        print("Capabilities release")
        cap.release()
        index += 1
    return arr


print("Count Get:", load_known_faces())
